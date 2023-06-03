from django import forms
from django.forms import ModelForm
from .models import Vehiculo

class VehiculoForm(ModelForm):
    class Meta:
        model  = Vehiculo
        fields = ['patente','marca','modelo','categoria']

        widget = {
            'patente'  : forms.TextInput(attrs={'class':'form-control'}),
            'marca'    : forms.TextInput(attrs={'class':'form-control'}),
            'modelo'   : forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
        }