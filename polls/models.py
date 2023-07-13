from django.db import models

# Create your models here.
class Question(models.Model): # inherit from django.db.models.Model
    question_text = models.CharField(max_length=200) 
    # define question_text as CharField, max_length is essential
    pub_date = models.DateTimeField("date published")
    # the arguments represented the readable name for human

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # this function defined a relationship between Choice and Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)