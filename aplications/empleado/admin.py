from django.contrib import admin
from .models import Empleado, Habilidades
from django.contrib import admin
from django.http import HttpResponse
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.db import models
from ckeditor.widgets import CKEditorWidget
# Register your models here.https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingImports

admin.site.register(Habilidades)

#List_display: para ordenar por columnas los datos ingresados
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        "nombre", 
        "apellido",
        "trabajo",
        "departamento", 
    )
    
    fields=(
        'nombre',
        'apellido',
        'trabajo',
        'departamento',
        'habilidades',
        'observaciones')
    
    
    
    def export_selected_to_csv(modeladmin, request, queryset):
        response= HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename ="empleados_seleccionado"'
        
        csv_writer= csv.writer(response)
        csv_writer.writerow(["nombre", "apellido", "trabajo"])
        for Empleado in queryset:
            csv_writer.writerow([
            Empleado.nombre,
            Empleado.apellido,
            Empleado.trabajo,
        ])
        return response
    export_selected_to_csv.short_description= "exportar empleados en CSV"
    
    def export_selected_to_pdf(modeladmin, request, queryset):

         response = HttpResponse(content_type='application/pdf')
         response['Content-Disposition'] = 'attachment; filename="articulos.pdf"'

         p = canvas.Canvas(response, pagesize=(595, 842))  # Tamaño A4

    # Define el contenido del PDF aquí usando ReportLab
    # Por ejemplo:
         p.drawString(100, 750, "")
         y = 720
         for item in queryset:
            p.drawString(120, y, f"{item.nombre}")
            p.drawString(120, y - 20, f"{item.apellido}")
            p.drawString(120, y - 40, f"{item.trabajo}")
            y -= 90

    # Cerrar el lienzo PDF
         p.showPage()
         p.save()

         return response

    export_selected_to_pdf.short_description = "Exportar elementos seleccionados a PDF"
    
    actions=[export_selected_to_csv, export_selected_to_pdf]   


    
admin.site.register(Empleado, EmpleadoAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    formfield_overrides= {
        models.TextField:{'Widgets': CKEditorWidget()},
    }

