from django.shortcuts import render
from pacientes.models import Paciente
from pacientes.forms import DonanteReposicionForm, EditarPacienteForm, PacienteAsignadoForm

from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

def listadoPaciente(request):
    pacientes_requeridos = {'listado_pac_req': Paciente.objects.order_by('id'), 'cant_pac': Paciente.objects.count()}
    return render(request, 'pacientes/listado.html', pacientes_requeridos)

def nuevoPaciente(request):
    if request.method == 'POST':
        formaDonanteReposicion = DonanteReposicionForm(request.POST)
        if formaDonanteReposicion.is_valid():
            formaDonanteReposicion.save()
            return redirect('listadoPaciente')
    else:
        formaDonanteReposicion = DonanteReposicionForm()

    formaDonanteReposicion = {'formaDonanteReposicion': DonanteReposicionForm()}
    return render(request, 'pacientes/nuevo.html', formaDonanteReposicion)

def detallePaciente(request, id):
    paciente_detalle = {'detalle_pac': get_object_or_404(Paciente, pk=id)}
    return render(request, 'pacientes/detalle.html', paciente_detalle)

def editarPaciente(request, id):
    editarPaciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        formaPaciente = EditarPacienteForm(request.POST, instance=editarPaciente)
        if formaPaciente.is_valid():
            formaPaciente.save()
            return redirect('listadoPaciente')
    else:
        formaPaciente = EditarPacienteForm(instance=editarPaciente)
    return render(request, 'pacientes/editar.html', {'formaPaciente': formaPaciente})

def eliminarPaciente(request, id):
    eliminarPaciente = get_object_or_404(Paciente, pk=id)
    if eliminarPaciente:
        eliminarPaciente.delete()
    return redirect('listadoPaciente')

def aplicarNuevaReposicion(request, id):

    if request.method == 'POST':
        formaReposicionAsignada = {PacienteAsignadoForm(request.POST)}

        if formaReposicionAsignada.is_valid():
            formaReposicionAsignada.save()
            return redirect('listadoPaciente')
    else:
        formaReposicionAsignada = PacienteAsignadoForm()

    formaReposicionAsignada = {'formaReposicionAsignada': PacienteAsignadoForm()}
    return render(request, 'pacientes/aplicarPaciente.html', formaReposicionAsignada)



