# Generated by Django 4.2.4 on 2023-10-13 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=['img/'], verbose_name='Imagen'),
        ),
    ]