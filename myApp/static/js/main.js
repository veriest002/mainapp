
$(function () {

	var $sidebar = $(".side-menu"),
		$window = $(window),
		offset = $sidebar.offset(),
		threshold = 150 + $sidebar.height(); // may need to tweak
	topPadding = 15;

	$window.scroll(function () {
		if ($window.scrollTop() > threshold) {
			$sidebar.stop().animate({
				marginTop: threshold
			});
		} else if ($window.scrollTop() > offset.top) {
			$sidebar.stop().animate({
				marginTop: $window.scrollTop() - offset.top + topPadding
			});
		} else {
			$sidebar.stop().animate({
				marginTop: 0
			});
		}
	});

});





$(document).ready(function () {



	//first inputs form name and description

	$(document).on("focus", ".text-one", function () {

		$(this).parent().parent().css({ "border-left": "3px solid #4d90fe" });

	}).on("blur", ".text-one", function () {
		$(this).parent().parent().css({ "border-left": "0" });
	});

	//tootlips and jquery ui initializers
	
	$('[data-toggle="tooltip"]').tooltip();
	
	$("#sortable").sortable();
	
	$(".add-question").on("click", function () {
		$(".onclick-menu").toggle("fast");
	
	});
	
	//tootlips and jquery ui initializers

});

//first inputs form name and description




//dynamic created input fields borders

$(document).on("focus", ".question-text, .option", function () {

	$(this).closest(".questions").css({ "border-left": "3px solid #4d90fe" });


	console.log(2);


}).on("blur", ".question-text, .option", function () {
	$(this).closest(".questions").css({ "border-left": "0" });
});

//dynamic created input fields borders





//Add options for the question

$(document).on("click", ".option-add", function () {

	$(this).closest(".question-container").find(".dynamic-content").append(
		'<div class="questions-con">' +
		'<h5 style="float: left; margin-left: 15px;"><i class="material-icons radio-icon">&#xe836;</i></h5>' +
		'<input type="text" class="option" name="ques" placeholder="option">' +
		'<span class="highlight"></span>' +
		' <span class="bar-ques"></span>' +
		'<span class="remove-option" style="position: relative; top: -20px; left: 40%; color: rgba(0, 0, 0, 0.32); cursor:pointer;"><i class="material-icons">&#xe5cd;</i></span>' +
		'</div>'
	);

});

//Add options Checkboxes
$(document).on("click", ".option-add-check", function () {

	$(this).closest(".question-container").find(".dynamic-content").append(
		'<div class="questions-con">' +
		'<h5 style="float: left; margin-left: 15px;"><i class="material-icons check-icon">&#xe835;</i></h5>' +
		'<input type="text" class="option" name="ques" placeholder="option">' +
		'<span class="highlight"></span>' +
		' <span class="bar-ques"></span>' +
		'<span class="remove-option" style="position: relative; top: -20px; left: 40%; color: rgba(0, 0, 0, 0.32); cursor:pointer;"><i class="material-icons">&#xe5cd;</i></span>' +
		'</div>'
	);

});

//Add options for the question


//remove question option

$(document).on("click", ".remove-option", function () {

	$(this).closest(".questions-con").remove();

});

//remove question option

//mouse over effect for borders

$(document).on("mouseover", ".questions", function () {

	$(this).css({ "box-shadow": "0px 5px 5px 0px #aaaaaa" });

}).on("mouseleave", ".questions", function () {

	$(this).css({ "box-shadow": "0 0 0 0 #aaaaaa" });

});

//mouse over effect for borders




$(document).ready(function () {



	$(".add-question").click(function () {

		$("#sortable").append(
			'<div class="ui-state-default questions"><hr><span class="ui-icon ui-icon-arrowthick-2-n-s">...</span><br><hr>' +
			'<div style="display: inline-block;">' +
			'<div style="float: left;">' +
			'<input class="question-text" type="text" value="Untitled Question" required>' +
			'<span class="highlight"></span>' +
			'<span class="bar-question"></span>' +
			'</div>' +
			'<div style="float: right; margin-top: 15px; margin-left: 25px;">' +
			'<select id="type-question">' +
			'<option value="1">Single Selection</option>' +
			'<option value="2">Multiple Selection</option>' +
			'<option value="3">Numeric Value</option>' +
			'</select>' +
			'</div>' +
			'</div>' +
			'<br>' +
			'<div class="questions-survey">' +
			'<div class="form-group">' +
			'<div class="question-container" style="margin-left: 40px;">' +
			'<div class="dynamic-content" style="margin-bottom: 15px;">' +
			'<div class="questions-con">' +
			'<h5 style="float: left; margin-left: 15px;"><i class="material-icons radio-icon">&#xe836;</i></h5>' +
			'<input type="text" class="option" name="ques" placeholder="option">' +
			'<span class="highlight"></span>' +
			'<span class="bar-ques"></span>' +
			'<span class="remove-option" style="position: relative; top: -20px; left: 40%; color: rgba(0, 0, 0, 0.32); cursor:pointer;"><i class="material-icons">&#xe5cd;</i></span>' +
			'</div>' +
			'</div>' +
			'<div class="static-content">' +
			'<h5 style="float: left; margin-left: 15px;"><i class="material-icons radio-icon">&#xe836;</i></h5>' +
			'<input type="text" class="option-add" name="ques" placeholder="Add option">' +
			'<span class="highlight"></span>' +
			'<span class="bar-ques"></span>' +
			'</div>' +
			'</div>' +
			'</div>' +
			'</div>' +
			'<hr>' +
			'<h3><span class="delete-question"><i class="material-icons">&#xe872;</i></span></h3>' +
			'</div>'

		);

	});


	//drop down selector for change of question types
	$(document).on("change", "#type-question", function () {

		if ($(this).val() == 1) {
			console.log(1);

			$(this).closest(".questions").replaceWith(
				'<div class="ui-state-default questions"><hr><span class="ui-icon ui-icon-arrowthick-2-n-s">...</span><br><hr>' +
				'<div style="display: inline-block;">' +
				'<div style="float: left;">' +
				'<input class="question-text" type="text" value="Untitled Question" required>' +
				'<span class="highlight"></span>' +
				'<span class="bar-question"></span>' +
				'</div>' +
				'<div style="float: right; margin-top: 15px; margin-left: 25px;">' +
				'<select id="type-question">' +
				'<option value="1">Single Selection</option>' +
				'<option value="2">Multiple Selection</option>' +
				'<option value="3">Numeric Value</option>' +
				'</select>' +
				'</div>' +
				'</div>' +
				'<br>' +
				'<div class="questions-survey">' +
				'<div class="form-group">' +
				'<div class="question-container" style="margin-left: 40px;">' +
				'<div class="dynamic-content" style="margin-bottom: 15px;">' +
				'<div class="questions-con">' +
				'<h5 style="float: left; margin-left: 15px;"><i class="material-icons radio-icon">&#xe836;</i></h5>' +
				'<input type="text" class="option" name="ques" placeholder="option">' +
				'<span class="highlight"></span>' +
				'<span class="bar-ques"></span>' +
				'<span class="remove-option" style="position: relative; top: -20px; left: 40%; color: rgba(0, 0, 0, 0.32); cursor:pointer;"><i class="material-icons">&#xe5cd;</i></span>' +
				'</div>' +
				'</div>' +
				'<div class="static-content">' +
				'<h5 style="float: left; margin-left: 15px;"><i class="material-icons radio-icon">&#xe836;</i></h5>' +
				'<input type="text" class="option-add" name="ques" placeholder="Add option">' +
				'<span class="highlight"></span>' +
				'<span class="bar-ques"></span>' +
				'</div>' +
				'</div>' +
				'</div>' +
				'</div>' +
				'<hr>' +
				'<h3><span class="delete-question"><i class="material-icons">&#xe872;</i></span></h3>' +
				'</div>'
			)
		}
		if ($(this).val() == 2) {
			console.log(2);

			$(this).closest(".questions").replaceWith(
				'<div class="ui-state-default questions"><hr><span class="ui-icon ui-icon-arrowthick-2-n-s">...</span><br><hr>' +
				'<div style="display: inline-block;">' +
				'<div style="float: left;">' +
				'<input class="question-text" type="text" value="Untitled Question" required>' +
				'<span class="highlight"></span>' +
				'<span class="bar-question"></span>' +
				'</div>' +
				'<div style="float: right; margin-top: 15px; margin-left: 25px;">' +
				'<select id="type-question">' +
				'<option value="2">Multiple Selection</option>' +
				'<option value="1">Single Selection</option>' +
				'<option value="3">Numeric Value</option>' +
				'</select>' +
				'</div>' +
				'</div>' +
				'<br>' +
				'<div class="questions-survey">' +
				'<div class="form-group">' +
				'<div class="question-container" style="margin-left: 40px;">' +
				'<div class="dynamic-content" style="margin-bottom: 15px;">' +
				'<div class="questions-con">' +
				'<h5 style="float: left; margin-left: 15px;"><i class="material-icons check-icon">&#xe835;</i></h5>' +
				'<input type="text" class="option" name="ques" placeholder="option">' +
				'<span class="highlight"></span>' +
				'<span class="bar-ques"></span>' +
				'<span class="remove-option" style="position: relative; top: -20px; left: 40%; color: rgba(0, 0, 0, 0.32); cursor:pointer;"><i class="material-icons">&#xe5cd;</i></span>' +
				'</div>' +
				'</div>' +
				'<div class="static-content">' +
				'<h5 style="float: left; margin-left: 15px;"><i class="material-icons check-icon">&#xe835;</i></h5>' +
				'<input type="text" class="option-add-check" name="ques" placeholder="Add option">' +
				'<span class="highlight"></span>' +
				'<span class="bar-ques"></span>' +
				'</div>' +
				'</div>' +
				'</div>' +
				'</div>' +
				'<hr>' +
				'<h3><span class="delete-question"><i class="material-icons">&#xe872;</i></span></h3>' +
				'</div>'
			)


		}
		if ($(this).val() == 3) {

			$(this).closest(".questions").replaceWith(
				'<div class="ui-state-default questions"><hr><span class="ui-icon ui-icon-arrowthick-2-n-s">...</span><br><hr>' +
				'<div style="display: inline-block;">' +
				'<div style="float: left;">' +
				'<input class="question-text" type="text" value="Untitled Question" required>' +
				'<span class="highlight"></span>' +
				'<span class="bar-question"></span>' +
				'</div>' +
				'<div style="float: right; margin-top: 15px; margin-left: 25px;">' +
				'<select id="type-question">' +
				'<option value="3">Numeric Value</option>' +
				'<option value="2">Multiple Selection</option>' +
				'<option value="1">Single Selection</option>' +
				'</select>' +
				'</div>' +
				'</div>' +
				'<br>' +
				'<div class="questions-survey">' +
				'<div class="form-group">' +
				'<div class="question-container" style="margin-left: 40px;">' +
				'<div class="numeric-question">' +
				'<input type="text" class="option" name="ques" placeholder="Numeric Value" disabled="true">' +
				'<span class="highlight"></span>' +
				'<span class="bar-ques"></span>' +
				'</div>' +
				'</div>' +
				'</div>' +
				'</div>' +
				'<hr>' +
				'<h3><span class="delete-question"><i class="material-icons">&#xe872;</i></span></h3>' +
				'</div>'
			)



			console.log(3);
		}
	});


	//deletes whole question

	$(document).on("click", ".delete-question", function () {


		$(this).closest(".questions").remove();

	});
});


Survey
    .StylesManager
    .applyTheme("default");

var json = {
    questions: [
        {
            type: "rating",
            name: "satisfaction",
            title: "How satisfied are you with the Product?",
            minRateDescription: "Not Satisfied",
            maxRateDescription: "Completely satisfied"
        }
    ]
};

window.survey = new Survey.Model(json);

survey
    .onComplete
    .add(function (result) {
        document
            .querySelector('#surveyResult')
            .innerHTML = "result: " + JSON.stringify(result.data);
    });

$("#surveyElement").Survey({model: survey});

