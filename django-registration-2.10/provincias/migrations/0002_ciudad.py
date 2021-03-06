# Generated by Django 4.0.4 on 2022-04-22 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provincias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCiudad', models.CharField(max_length=255)),
                ('codigoPostal', models.IntegerField()),
                ('idProvincia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='provincias.provincia')),
            ],
        ),
    ]
