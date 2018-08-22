from django.forms import ModelForm,modelformset_factory,inlineformset_factory,models
from myApp.models import Survey, Question, Response, Answer
from django.utils.translation import ugettext_lazy as _
from builtins import int, object, super

from django import forms
from django.urls import reverse
from django.utils.text import slugify
from myApp.signal import survey_completed

import logging
LOGGER = logging.getLogger(__name__)

class SurveyForm(ModelForm):
    class Meta(object):
        model = Survey
        fields = '__all__'
        # labels = {
        #     'name': _("ชื่อแบบฟอร์ม"),
        #     'description': _("คำอธิบาย")
        # }

class QuestionForm(ModelForm):
    class Meta(object):
        model = Question
        fields="__all__"

# QuestionFormSet = modelformset_factory(
#     model = Question,
#     form = QuestionForm,
#     extra=2,
# )

QuestionInlineFormSet = inlineformset_factory(
    parent_model = Survey,
    model = Question,
    extra = 0,
    fields = "__all__",
    # formset=QuestionFormSet,
    min_num=1,
)

class ResponseForm(models.ModelForm):

    WIDGETS = {
        Question.TEXT: forms.Textarea,
        Question.SHORT_TEXT: forms.TextInput,
        Question.RADIO: forms.RadioSelect,
    }

    class Meta(object):
        model = Response
        fields = ()

    def __init__(self, *args, **kwargs):
        """ Expects a survey object to be passed in initially """
        self.survey = kwargs.pop('survey')
        self.user = kwargs.pop('user')
        try:
            self.step = int(kwargs.pop('step'))
        except KeyError:
            self.step = None
        super(ResponseForm, self).__init__(*args, **kwargs)
        self.steps_count = len(self.survey.questions.all())
        # add a field for each survey question, corresponding to the question
        # type as appropriate.
        data = kwargs.get('data')
        for i, question in enumerate(self.survey.questions.all()):
            is_current_step = i != self.step and self.step is not None
            self.add_question(question, data)

    def _get_preexisting_response(self):
        """ Recover a pre-existing response in database.

        The user must be logged.
        :rtype: Response or None"""
        if not self.user.is_authenticated:
            return None
        try:
            return Response.objects.get(user=self.user, survey=self.survey)
        except Response.DoesNotExist:
            LOGGER.debug("No saved response for '%s' for user %s",
                         self.survey, self.user)
            return None

    def _get_preexisting_answer(self, question):
        """ Recover a pre-existing answer in database.

        The user must be logged. A Response containing the Answer must exists.

        :param Question question: The question we want to recover in the
        response.
        :rtype: Answer or None"""
        response = self._get_preexisting_response()
        if response is None:
            return None
        try:
            return Answer.objects.get(question=question, response=response)
        except Answer.DoesNotExist:
            return None

    def get_question_initial(self, question, data):
        """ Get the initial value that we should use in the Form

        :param Question question: The question
        :param dict data: Value from a POST request.
        :rtype: String or None  """
        initial = None
        answer = self._get_preexisting_answer(question)
        if answer:
            # Initialize the field with values from the database if any
            initial = answer.body
        if data:
            # Initialize the field field from a POST request, if any.
            # Replace values from the database
            initial = data.get('question_%d' % question.pk)
        return initial

    def get_question_widget(self, question):
        """ Return the widget we should use for a question.

        :param Question question: The question
        :rtype: django.forms.widget or None """
        try:
            return self.WIDGETS[question.type]
        except KeyError:
            return None

    def get_question_choices(self, question):
        """ Return the choices we should use for a question.

        :param Question question: The question
        :rtype: List of String or None """
        qchoices = None
        if question.type not in [Question.TEXT, Question.SHORT_TEXT]:
            qchoices = question.get_choices()
            # add an empty option at the top so that the user has to explicitly
            # select one of the options
        return qchoices

    def get_question_field(self, question, **kwargs):
        """ Return the field we should use in our form.

        :param Question question: The question
        :param **kwargs: A dict of parameter properly initialized in
            add_question.
        :rtype: django.forms.fields """
        FIELDS = {
            Question.TEXT: forms.CharField,
            Question.SHORT_TEXT: forms.CharField,
        }
        # logging.debug("Args passed to field %s", kwargs)
        try:
            return FIELDS[question.type](**kwargs)
        except KeyError:
            return forms.ChoiceField(**kwargs)

    def add_question(self, question, data):
        """ Add a question to the form.

        :param Question question: The question to add.
        :param dict data: The pre-existing values from a post request. """
        kwargs = {"label": question.text,
                  "required": question.required, }
        initial = self.get_question_initial(question, data)
        if initial:
            kwargs["initial"] = initial
        choices = self.get_question_choices(question)
        if choices:
            kwargs["choices"] = choices
        widget = self.get_question_widget(question)
        if widget:
            kwargs["widget"] = widget
        field = self.get_question_field(question, **kwargs)
        # logging.debug("Field for %s : %s", question, field.__dict__)
        self.fields['question_%d' % question.pk] = field

    def has_next_step(self):
        if self.step < self.steps_count - 1:
            return True
        return False

    def next_step_url(self):
        if self.has_next_step():
            context = {'id': self.survey.id, 'step': self.step + 1}
            return reverse('survey-detail-step', kwargs=context)
        else:
            return None

    def current_step_url(self):
        return reverse('survey-detail-step',
                       kwargs={'id': self.survey.id, 'step': self.step})

    def save(self, commit=True):
        """ Save the response object """
        # Recover an existing response from the database if any
        #  There is only one response by logged user.
        response = self._get_preexisting_response()
        if response is None:
            response = super(ResponseForm, self).save(commit=False)
        response.survey = self.survey
        if self.user.is_authenticated:
            response.user = self.user
        response.save()
        # response "raw" data as dict (for signal)
        data = {
            'survey_id': response.survey.id,
            'responses': []
        }
        # create an answer object for each question and associate it with this
        # response.
        for field_name, field_value in self.cleaned_data.items():
            if field_name.startswith("question_"):
                # warning: this way of extracting the id is very fragile and
                # entirely dependent on the way the question_id is encoded in
                # the field name in the __init__ method of this form class.
                q_id = int(field_name.split("_")[1])
                question = Question.objects.get(pk=q_id)
                answer = self._get_preexisting_answer(question)
                if answer is None:
                    answer = Answer(question=question)
                answer.body = field_value
                data['responses'].append((answer.question.id, answer.body))
                LOGGER.debug(
                    "Creating answer for question %d of type %s : %s", q_id,
                    answer.question.type, field_value
                )
                answer.response = response
                answer.save()
        survey_completed.send(sender=Response, instance=response, data=data)
        return response
