# Generated by Django 5.1.2 on 2024-10-25 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EspacioOOH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('ubicacion', models.CharField(max_length=255)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('precio_vendido', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.CharField(max_length=255)),
                ('espacio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ooh.espacioooh')),
            ],
        ),
    ]
