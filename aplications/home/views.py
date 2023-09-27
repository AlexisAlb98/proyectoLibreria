from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Prueba

class IndexView (TemplateView):
    template_name='home/home.html'
    


class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/lista_prueba.html"
    context_object_name= "lista_prueba"
