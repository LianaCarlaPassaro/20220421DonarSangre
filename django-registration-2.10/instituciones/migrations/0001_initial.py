# Generated by Django 4.0.4 on 2022-04-22 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provincias', '0002_ciudad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreInstitucion', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('idCiudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='provincias.ciudad')),
            ],
        ),
    ]
