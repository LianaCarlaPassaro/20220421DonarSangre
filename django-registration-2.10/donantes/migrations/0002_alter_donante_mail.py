# Generated by Django 4.0.4 on 2022-05-07 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donante',
            name='mail',
            field=models.EmailField(max_length=255),
        ),
    ]