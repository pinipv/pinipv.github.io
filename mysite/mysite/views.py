from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404

from ..polls.models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def second(request):
    return HttpResponse("Segunda paguna")

def detail(request,question_id):
    #try:
    #    question= Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exists")
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/datail.html',{'question':question})

def index(request):
    lista = Question.object.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'lista':lista}
    
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)