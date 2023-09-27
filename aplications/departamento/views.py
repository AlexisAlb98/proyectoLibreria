from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Departamento

class DepartametoListView (TemplateView):
    model = Departamento
    template_name = "departamento/Tabla.html"
    context_object_name= "tabla"