# Generated by Django 4.2.4 on 2023-10-07 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_proveedor_remove_producto_editorial_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades del empleado',
                'ordering': ['habilidad'],
                'unique_together': {('habilidad',)},
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='Habilidades',
            field=models.ManyToManyField(to='productos.habilidades'),
        ),
    ]
