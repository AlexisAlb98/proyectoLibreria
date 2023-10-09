from django.db import models

# Create your models here.
class proveedor (models.Model):
    codigo_proveedor = models.AutoField(primary_key=True, unique=True)
    nombre_empresa = models.CharField("Nombre de la empresa:", max_length=30, blank=True)
    sigla= models.CharField("Sigla:", max_length=30)
    activo =models.BooleanField("Esta activo?:", default=False)
    direccion= models.CharField("Dirección:", max_length=30, blank=True)
    telefono = models.CharField("Teléfono:",max_length=15, blank=True)
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores de la empresa"
        ordering=["nombre_empresa"]
        unique_together = ("nombre_empresa", "sigla",)
        
    
    def __str__(self):
        return self.nombre_empresa + '-' + self.sigla + '-'+ self.direccion + '-' + self.telefono