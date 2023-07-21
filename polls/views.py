from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    # order the 5 latest questions
    context={"latest_question_list":latest_question_list}
    return render(request,"polls/index.html",context)
    # load polls/index.html and pass it with context which is a dict used for mapping using render()

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})

def results(request,question_id):
    response="You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)
