from django import forms
from .models import Servicio, Superficie, cancha, Horario, CentroDeportivo, Tipo_cancha, Provincias, Regiones, Comunas
from django.contrib import admin
from django.forms import *

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre del servicio',
        }
        widgets = {
            'nombre': TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese nombre',
                    'id': 'nombre',
            })
        }

class SuperficieForm(ModelForm):
    class Meta:
        model = Superficie
        fields = ['nombre']

class TipoForm(ModelForm):
    class Meta:
        model = Tipo_cancha
        fields = ['nombre']

class CanchaForm(ModelForm):
    class Meta:
        model = cancha
        fields = ['nombre','descripcion','direccion','valor','servicios','tipo_cancha','superfice','centro_dep']

class HorarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = ['cancha','hora_inicio','hora_termino','dia']

class CentroForm(ModelForm):
    class Meta:
        model = CentroDeportivo
        fields = ['Nombre' , 'direccion', 'region', 'provincia', 'comuna']
        labels = {
            'Nombre': 'Nombre del centro',
            'direccion': 'Direccion',
            'region': 'Region',
            'provincia': 'Provincia',
            'comuna': 'Comuna',
            }
        

    
  




    

  

    
    



  

