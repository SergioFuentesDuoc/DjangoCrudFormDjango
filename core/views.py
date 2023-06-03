from django.shortcuts import render, redirect
from .models import Vehiculo
from .form import VehiculoForm

# Create your views here.

def home(request):

    vehiculos = Vehiculo.objects.all()
    datos = {
        'vehiculos':vehiculos
    }

    return render(request, 'core/home.html', datos)


def form_vehiculo(request):
    datos = {
        'form':VehiculoForm()
    }
    if request.method=='POST':
        formulario= VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
    return render(request, 'core/form_vehiculo.html', datos)



def form_mod_vehiculo(request, id):
    auto = Vehiculo.objects.get(patente=id)
    datos = {
        'form':VehiculoForm()
    }
    if request.method=='POST':
        formulario = VehiculoForm(data=request.POST, intance=auto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados Correctamente"
    return render(request, 'core/form_mod_vehiculo.html', datos)


def listar_mod_vehiculo(request):
    vehiculos = Vehiculo.objects.all()
    datos = {
        'vehiculos':vehiculos
    }
    return render(request, 'core/listar_mod_vehiculo.html', datos)




