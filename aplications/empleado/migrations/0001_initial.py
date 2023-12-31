# Generated by Django 4.2.4 on 2023-09-11 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0002_alter_departamento_piso_alter_departamento_sigla'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=60, verbose_name='Apellido')),
                ('trabajo', models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRATIVO'), ('2', 'DESARROLLADOR'), ('3', 'ANALISTA FUNCIONAL'), ('4', 'OTRO')], max_length=1, verbose_name='Puesto')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
        ),
    ]
