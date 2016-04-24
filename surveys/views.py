from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Survey

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'surveys/index.html'
	context_object_name = 'survey_list'
	queryset = Survey.objects.all()
	

class DetailView(generic.DetailView):
	model = Survey
	template_name = 'surveys/detail.html'

def report(request, survey_id):
	survey = get_object_or_404(Survey, pk=survey_id)
	question_array = [question.id for question in survey.question_set.all()]
	value_array = [request.GET['question'+str(question_id)] for question_id in question_array]

	result = sum(int(x) for x in value_array)
	return HttpResponse(str(result))