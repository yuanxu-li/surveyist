from django.db import models

# Create your models here.
class Survey(models.Model):
	SURVEY_TYPE = (
		('health', 'Health'),
		('computer', 'Computer'),
		('psychology', 'Psychology'),
		('other', 'Other')
	)
	name = models.CharField(max_length=60)
	survey_type = models.CharField(max_length=60, choices=SURVEY_TYPE)

	def __str__(self):
		return self.name

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	update_date = models.DateField(auto_now_add=True)
	survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	value = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text