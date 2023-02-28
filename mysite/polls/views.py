from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404

from .models import Question, Product



from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from pymongo import MongoClient




class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'products_list'
    
    def get_queryset(self):
        
        return Product.objects.all()
        
class PruebaView(generic.ListView):
    template_name = 'polls/prueba.html'
    context_object_name = 'prubas_list'
    
    def get_queryset(self):
        return 1

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
def sumar(numero):
    return numero+2
    
def Prueba(request):
#    template = loader.get_template('polls/prueba.html')
    string="mongodb+srv://adri_pv:qazxswedc21324354@easy.yvxgjtg.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(string)
    dbname = client.easy_db
    tabla = dbname.easy_t
    datos = tabla.find({})
    
    context = datos
    return render(request, 'polls/prueba.html', {'datos':context})