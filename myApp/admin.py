from django.contrib import admin
from myApp.models import Survey, Question, Answer, Response
# from django.http import HttpResponse
# from django.contrib.auth.models import User

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class SurveyAdmin(admin.ModelAdmin):
	list_display = ['name', 'description']
	inlines = [QuestionInline]

# def export_xls(modeladmin, request, queryset):
#     import xlwt
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=mymodel.xls'
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet("MyModel")
    
#     row_num = 0
    
#     columns = [
#         (u"User", 2000),
#         (u"Answer", 2000),
#     ]

#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True

#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num][0], font_style)
#         # set column width
#         ws.col(col_num).width = columns[col_num][1]

#     font_style = xlwt.XFStyle()
#     font_style.alignment.wrap = 1
    
#     for obj in queryset:
#         row_num += 1
#         row = [
#             Response.objects.all()
#         ]
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)
            
#     wb.save(response)
#     return response
    
# export_xls.short_description = u"Export XLS"

class AnswerBaseInline(admin.StackedInline):
    fields = ('question', 'body')
    readonly_fields = ('question',)
    extra = 0
    model = Answer

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('survey', 'created', 'user')
    list_filter = ('survey', 'created')
    date_hierarchy = 'created'
    inlines = [AnswerBaseInline]
    # specifies the order as well as which fields to act on
    readonly_fields = (
        'survey', 'created', 'updated','user'
    )
    # actions = [export_xls]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Response, ResponseAdmin)

# Register your models here.
# from myApp.models import Person
# class PersonAdmin(admin.ModelAdmin):
# 	list_display=[f.name for f in Person._meta.fields]
# admin.site.register(Person,PersonAdmin)