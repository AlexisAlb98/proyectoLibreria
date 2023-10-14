from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Empleado

# Create your views here.
class EmpleadoListView (TemplateView):
    model = Empleado
    template_name = "empleado/list_empleado.html"
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/list_empleado.html"
    context_object_name= "Empleado"


def get_queryset(self):
    productos = Empleado.objects.get()
    return productos.all()