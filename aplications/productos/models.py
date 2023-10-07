from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Proveedor (models.Model):
    TIPO_CHOICES =(
    ("0", "LIBRO"),
    ("1", "PAPELERIA"),
    )
    
    codigo_proveedor = models.AutoField(primary_key=True, unique=True)
    nombre: models.CharField("Nombre", max_length=60, blank=True)
    Tipo_proveedor:models.CharField("Tipo de proveedor",max_length=4, blank=True, choices=TIPO_CHOICES)
    empresa: models.CharField("Nombre de la empresa", max_length=60, blank=True)
    editorial =models.BooleanField("Es una editorial?:", default=False)
    
    class Meta:
            verbose_name = "Proveedor"
            verbose_name_plural = "Proveedores"
            
    def __str__(self):
        return self.empresa + "-" + self.nombre
    
class Producto (models.Model):
   
    TIPO_CHOICES =(
    ("0", "LIBRO"),
    ("1", "PAPELERIA"),
    )
    OPCIONES_AÑO = (
        [(str(i), str(1930 + i)) for i in range(94)]
        )
    
    codigo = models.AutoField(primary_key=True, unique=True)
    producto = models.CharField("Producto", max_length=60, blank=True)
    Tipo_prod = models.CharField("Tipo de producto", max_length=1,choices= TIPO_CHOICES)
    Autor = models.CharField("Autor", max_length=60, blank=True)
    proveedor = models.ManyToManyField(Proveedor)
    año = models.CharField("Año",max_length=4, blank=True,choices=OPCIONES_AÑO)
    precio = models.DecimalField("Precio $", max_digits=10, decimal_places=2, blank=True, null=True,)
    imagen = models.ImageField("Imagen", upload_to=["img/suministro-libreria.png" ] ,blank=True)
    #Cod_barra=
    #stock_actual=
    descripcion = RichTextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Productos"
        ordering=["producto"]
        
    def __str__(self):
        return self.producto + "-" + self.Tipo_prod
