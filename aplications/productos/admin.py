from django.contrib import admin
from .models import Producto
from django.contrib import admin
from django.http import HttpResponse
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Producto

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    formfield_overrides= {
        models.TextField:{'Widgets': CKEditorWidget()},
    }
    
class ProductoAdmin(admin.ModelAdmin):
    list_display=(
        "codigo_producto",
        "producto", 
        "Tipo_prod",
        "descripcion")
    
    

admin.site.register(Producto, ProductoAdmin)
