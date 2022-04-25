# Generated by Django 4.0.4 on 2022-04-22 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provincias', '0002_ciudad'),
        ('instituciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('tipoDNI', models.CharField(choices=[('DNI', 'DNI'), ('LE', 'LE'), ('LC', 'LC')], max_length=255)),
                ('dni', models.CharField(max_length=255)),
                ('fechaNacimiento', models.DateField()),
                ('fechaLimite', models.DateField()),
                ('cantidadDonantes', models.IntegerField()),
                ('mail', models.CharField(max_length=255)),
                ('comentario', models.TextField(max_length=1024)),
                ('completo', models.BooleanField(default=False)),
                ('telefono', models.CharField(max_length=255)),
                ('tipoSangre', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('O+', 'O+'), ('O-', 'O-'), ('B+', 'B+'), ('AB+', 'AB+')], max_length=255)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('U', 'No Informa')], max_length=1)),
                ('ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='provincias.ciudad')),
                ('institucion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instituciones.institucion')),
            ],
        ),
    ]
