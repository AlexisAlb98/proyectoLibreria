from django.db import models
from ckeditor.fields import RichTextField
from aplications.proveedor.models import proveedor
# Create your models here.
class Articulos (models.Model):
   
    TIPO_CHOICES =(
    ("0", "LIBRO"),
    ("1", "PAPELERIA"),
    )
    OPCIONES_AÑO = (
        [(str(i), str(1930 + i)) for i in range(94)]
        )
    
    producto = models.CharField("Producto", max_length=60, blank=True)
    Tipo_prod = models.CharField("Tipo de producto", max_length=1,choices= TIPO_CHOICES)
    Autor = models.CharField("Autor", max_length=60, blank=True)
    proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    año = models.CharField("Año",max_length=4, blank=True,choices=OPCIONES_AÑO)
    precio = models.DecimalField("Precio $", max_digits=10, decimal_places=2, blank=True, null=True,)
    imagen = models.ImageField("Imagen", upload_to='uploads/'  ,blank=True)
    descripcion = RichTextField(blank=True, null=True)
    #Cod_barra=
    #stock_actual=
    
    
    class Meta:
        verbose_name_plural = "Articulos"
        ordering=["producto"]
        
    def __str__(self):
        return self.producto + "-" + self.Tipo_prod