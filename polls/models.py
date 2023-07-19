import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model): # inherit from django.db.models.Model
    question_text = models.CharField(max_length=200) 
    # define question_text as CharField, max_length is essential
    pub_date = models.DateTimeField("date published")
    # the arguments represented the readable name for human
    def __str__(self):
        return self.question_text
    # when we use the print(Q) where Q is a Question, python will print Q.__str__()
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # the return value of timedelta() can participate in date calculation and it's 
    # the easiest way to perform date manipulation

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # this function defined a relationship between Choice and Question
    # CASCADE implies that the relationship should be 1:N
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text