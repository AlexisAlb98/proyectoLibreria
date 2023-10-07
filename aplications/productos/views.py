from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Producto

# Create your views here.
class ProductoListView (TemplateView):
    model = Producto
    template_name = "productos/productos.html"
    context_object_name= "Productos"
