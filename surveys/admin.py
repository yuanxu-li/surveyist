from django.contrib import admin

from .models import Survey, Question, Choice
# Register your models here.

class QuestionInline(admin.TabularInline):
	model = Question
	extra = 3

class SurveyAdmin(admin.ModelAdmin):
	inlines = [QuestionInline]

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1

class QuestionAdmin(admin.ModelAdmin):
	inlines = [ChoiceInline]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)