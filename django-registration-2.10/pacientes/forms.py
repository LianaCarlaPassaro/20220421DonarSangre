from django.forms import ModelForm, EmailInput, DateInput
import django.forms.widgets
from django import forms


from pacientes.models import Paciente, ReposicionesAsignadas

# class DateInput(forms.DateInput):
#     input_type = 'date'
# class ExampleForm(forms.Form):
#     fechaNacimiento = forms.DateField(widget=DateInput)

class DonanteReposicionForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets ={
            'fechaNacimiento': forms.DateInput(attrs={'type':'date', 'data-date-format': 'dd-mm-yyyy', 'data-provide': 'datepicker'}, format="%d/%m/%Y"),
            'mail': EmailInput(attrs={'type': 'email'}),
            'fechaLimite': forms.DateInput(attrs={'type':'date', 'data-date-format': 'dd-mm-yyyy', 'data-provide': 'datepicker'}, format="%d/%m/%y"),
        }

class EditarPacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets ={
            'fechaNacimiento':  forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date'}),
            'mail': EmailInput(attrs={'type': 'email'}),
            'fechaLimite': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date'}),
        }
class PacienteAsignadoForm(ModelForm):
    class Meta:
        model = ReposicionesAsignadas
        fields = '__all__'
        widgets = {
            'fechaReposicionElegida': DateInput(attrs={'type':'date', 'data-date-format': 'dd-mm-yyyy', 'data-provide': 'datepicker'}, format="%d/%m/%Y"),

        }