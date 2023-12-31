# Generated by Django 4.2.4 on 2023-10-13 22:24

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedor', '0002_alter_proveedor_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(blank=True, max_length=60, verbose_name='Producto')),
                ('Tipo_prod', models.CharField(choices=[('0', 'LIBRO'), ('1', 'PAPELERIA')], max_length=1, verbose_name='Tipo de producto')),
                ('Autor', models.CharField(blank=True, max_length=60, verbose_name='Autor')),
                ('año', models.CharField(blank=True, choices=[('0', '1930'), ('1', '1931'), ('2', '1932'), ('3', '1933'), ('4', '1934'), ('5', '1935'), ('6', '1936'), ('7', '1937'), ('8', '1938'), ('9', '1939'), ('10', '1940'), ('11', '1941'), ('12', '1942'), ('13', '1943'), ('14', '1944'), ('15', '1945'), ('16', '1946'), ('17', '1947'), ('18', '1948'), ('19', '1949'), ('20', '1950'), ('21', '1951'), ('22', '1952'), ('23', '1953'), ('24', '1954'), ('25', '1955'), ('26', '1956'), ('27', '1957'), ('28', '1958'), ('29', '1959'), ('30', '1960'), ('31', '1961'), ('32', '1962'), ('33', '1963'), ('34', '1964'), ('35', '1965'), ('36', '1966'), ('37', '1967'), ('38', '1968'), ('39', '1969'), ('40', '1970'), ('41', '1971'), ('42', '1972'), ('43', '1973'), ('44', '1974'), ('45', '1975'), ('46', '1976'), ('47', '1977'), ('48', '1978'), ('49', '1979'), ('50', '1980'), ('51', '1981'), ('52', '1982'), ('53', '1983'), ('54', '1984'), ('55', '1985'), ('56', '1986'), ('57', '1987'), ('58', '1988'), ('59', '1989'), ('60', '1990'), ('61', '1991'), ('62', '1992'), ('63', '1993'), ('64', '1994'), ('65', '1995'), ('66', '1996'), ('67', '1997'), ('68', '1998'), ('69', '1999'), ('70', '2000'), ('71', '2001'), ('72', '2002'), ('73', '2003'), ('74', '2004'), ('75', '2005'), ('76', '2006'), ('77', '2007'), ('78', '2008'), ('79', '2009'), ('80', '2010'), ('81', '2011'), ('82', '2012'), ('83', '2013'), ('84', '2014'), ('85', '2015'), ('86', '2016'), ('87', '2017'), ('88', '2018'), ('89', '2019'), ('90', '2020'), ('91', '2021'), ('92', '2022'), ('93', '2023')], max_length=4, verbose_name='Año')),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio $')),
                ('imagen', models.ImageField(blank=True, upload_to=['img/suministro-libreria.png'], verbose_name='Imagen')),
                ('descripcion', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.proveedor')),
            ],
            options={
                'verbose_name_plural': 'Articulos',
                'ordering': ['producto'],
            },
        ),
    ]
