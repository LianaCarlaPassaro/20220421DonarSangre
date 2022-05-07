from django.db import models

# Create your models here.

from provincias.models import Ciudad
#from gruposFactor.models import GrupoFactor
#from sexo.models import Sexo
#from tipoDocumentos.models import TipoDocumento

class Donante(models.Model):
    SEX_OPTIONS = ((SEX_FEMALE := "F", "Femenino"), (SEX_MALE := "M", "Masculino"), (SEX_UNSURE := "U", "No Informa"))
    TIPO_DOCUMENTO = ((DNI := "DNI", "DNI"),(LE := "LE", "LE"), (LC := "LC", "LC"))
    GRUPO_FACTOR = ((A_POS := "A+", "A+"), (A_NEG := "A-", "A-"), (O_POS := "O+", "O+"), (O_NEG := "O-", "O-"), (B_POS := "B+", "B+"),(AB_POS := "AB+", "AB+"),)

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()
    #sexo = models.ForeignKey(Sexo, on_delete=models.SET_NULL, null=True)
    sexo = models.CharField(max_length=1, choices=SEX_OPTIONS)
    #tipoDNI = models.ForeignKey(TipoDocumento,on_delete=models.SET_NULL, null=True)
    tipoDNI = models.CharField(max_length=255, choices=TIPO_DOCUMENTO)
    dni = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    #tipoSangre = models.ForeignKey(GrupoFactor, on_delete=models.SET_NULL, null=True)
    tipoSangre = models.CharField(max_length=255, choices=GRUPO_FACTOR)
    fechaUltimaExtraccion = models.DateField()
    mail = models.EmailField(max_length=255)


    def __str__(self):
        return f'Donante: Nombre {self.nombre} Apellido: {self.apellido}'