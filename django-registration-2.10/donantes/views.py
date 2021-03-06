from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from donantes.forms import DonanteInscriptoForm, EditarDonanteForm
from donantes.models import Donante


def listadoDonante(request):
    donante_inscripto = {'listado_don_inscr': Donante.objects.order_by('id'), 'cant_don': Donante.objects.count()}
    return render(request, 'donantes/listado.html', donante_inscripto)

def detalleDonanteInscripto(request, id):
    donante_inscripto = {'detalle_don_insc': get_object_or_404(Donante, pk=id)}
    return render(request, 'donantes/detalle.html', donante_inscripto)

def editarDonanteInscripto(request, id):
    donanteInscripto = get_object_or_404(Donante, pk=id)
    if request.method == 'POST':
        formaDonanteInscripto = EditarDonanteForm(request.POST, instance=donanteInscripto)
        if formaDonanteInscripto.is_valid():
            formaDonanteInscripto.save()
            return redirect('listadoDonante')
    else:
        formaDonanteInscripto = EditarDonanteForm(instance=donanteInscripto)
    return render(request, 'donantes/editar.html', {'formaDonanteInscripto': formaDonanteInscripto})

def nuevoDonanteAInscribir(request):
    if request.method == 'POST':
        formaDonanteAInscribir = DonanteInscriptoForm(request.POST)
        if formaDonanteAInscribir.is_valid():
            formaDonanteAInscribir.save()
            return redirect('listadoDonante')
    else:
        formaDonanteAInscribir = DonanteInscriptoForm()

    formaDonanteAInscribir = {'formaDonanteAInscribir': DonanteInscriptoForm()}
    return render(request, 'donantes/nuevo.html', formaDonanteAInscribir)

def eliminarDonanteInscripto(request, id):
    donanteInscripto = get_object_or_404(Donante, pk=id)
    if donanteInscripto:
        donanteInscripto.delete()
    return redirect('listadoDonante')