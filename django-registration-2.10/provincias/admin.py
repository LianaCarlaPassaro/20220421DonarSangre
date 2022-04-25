from django.contrib import admin

# Register your models here.
from provincias.models import Provincia
from provincias.models import Ciudad
admin.site.register(Provincia)
admin.site.register(Ciudad)