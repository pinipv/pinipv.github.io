from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404

from .models import Question, Product



from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone




class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'products_list'
    
    def get_queryset(self):
        
        return Product.objects.all()
        


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.