from django.shortcuts import render

# Create your views here.
from .models import DestinosTuristicos
from django.shortcuts import render, redirect, get_object_or_404
from .models import DestinosTuristicos
from .forms import DestinoForm

def listar_destinos(request):

    destinos = DestinosTuristicos.objects.all()

    return render(
        request,
        'travello/destinos.html',
        {
            'destinos': destinos
        }
    )   
def añadir_destino(request):

    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('listar_destinos')

    else:
        form = DestinoForm()

    return render(
        request,
        'travello/crear_destino.html',
        {'form': form}
    )


def modificar_destino(request, pk):

    destino = get_object_or_404(
        DestinosTuristicos,
        pk=pk
    )

    if request.method == 'POST':

        form = DestinoForm(
            request.POST,
            request.FILES,
            instance=destino
        )

        if form.is_valid():
            form.save()
            return redirect('listar_destinos')

    else:

        form = DestinoForm(
            instance=destino
        )

    return render(
        request,
        'travello/modificar_destino.html',
        {'form': form}
    )


def eliminar_destino(request, pk):

    destino = get_object_or_404(
        DestinosTuristicos,
        pk=pk
    )

    if request.method == 'POST':

        destino.delete()

        return redirect(
            'listar_destinos'
        )

    return render(
        request,
        'travello/confirmar_eliminar.html',
        {'destino': destino}
    )