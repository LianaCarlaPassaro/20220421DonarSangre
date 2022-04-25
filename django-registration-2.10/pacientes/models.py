from django.db import models

# Create your models here.
from provincias.models import Ciudad
from instituciones.models import Institucion
from donantes.models import Donante


class Paciente(models.Model):
    SEX_OPTIONS = ((SEX_FEMALE := "F", "Femenino"), (SEX_MALE := "M", "Masculino"), (SEX_UNSURE := "U", "No Informa"))
    TIPO_DOCUMENTO = ((DNI := "DNI", "DNI"), (LE := "LE", "LE"), (LC := "LC", "LC"))
    GRUPO_FACTOR = (
    (A_POS := "A+", "A+"), (A_NEG := "A-", "A-"), (O_POS := "O+", "O+"), (O_NEG := "O-", "O-"), (B_POS := "B+", "B+"),
    (AB_POS := "AB+", "AB+"))

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    tipoDNI = models.CharField(max_length=255, choices=TIPO_DOCUMENTO)
    dni = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    institucion = models.ForeignKey(Institucion,  on_delete=models.SET_NULL, null=True)
    fechaLimite = models.DateField()
    cantidadDonantes = models.IntegerField()
    mail = models.CharField(max_length=255)
    comentario = models.TextField(max_length=1024)
    completo = models.BooleanField(default=False)
    telefono = models.CharField(max_length=255)
    tipoSangre = models.CharField(max_length=255, choices=GRUPO_FACTOR)
    sexo = models.CharField(max_length=1, choices=SEX_OPTIONS)

    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido} '

class ReposicionesAsignadas(models.Model):
    idPaciente = models.ForeignKey(Paciente,on_delete=models.SET_NULL, null=True)
    idDonante = models.ForeignKey(Donante, on_delete=models.SET_NULL, null=True)
    fechaReposicionElegida = models.DateField()
    comentario = models.TextField(max_length=1024)

    def __str__(self):
        return f'Paciente{self.idPaciente.nombre} id {self.idDonanteReposicion}'