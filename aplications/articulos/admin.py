from django.contrib import admin
from .models import Articulos
from django.contrib import admin
from django.http import HttpResponse
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Articulos

# Register your models here.


class ArticulosAdmin(admin.ModelAdmin):
    formfield_overrides= {
        models.TextField:{'Widgets': CKEditorWidget()},
    }
    
class ArticulosAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "producto", 
        "Tipo_prod",
        "descripcion")
    
    

admin.site.register(Articulos, ArticulosAdmin)