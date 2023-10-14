from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Articulos

# Create your views here.
class ArticulosListView (TemplateView):
    model = Articulos
    template_name = "articulos/articulos.html"
    

class ArticulosDetailView(DetailView):
    model = Articulos
    template_name = "articulos/articulos.html"
    context_object_name= "Articulos"


def get_queryset(self):
    productos = Articulos.objects.get()
    return productos.all()