from django import forms
from .models import Servicio, Superficie, Cancha, Horario, CentroDeportivo, Tipo_cancha, Provincias, Regiones, Comunas
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
        model = Cancha
        fields = ['usuario_id','nombre','descripcion','valor','servicios','tipo_cancha','superficie','centro_dep']

class HorarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = ['cancha','title','hora_inicio','hora_termino','dia', 'color']
        widgets = {
            'cancha': Select(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Nombre de cancha',
                    'id': 'cancha',
                }
            ),
            'title': HiddenInput(
                attrs = {
                    'id': 'title',
                    'value': 'Cerrado',
                }
            ),
            'hora_inicio': TimeInput(
                attrs = {
                    'class':'form-control',                    
                    'id': 'hora_inicio',
                    'type': 'time',
                }
            ),
            'hora_termino': TimeInput(
                attrs = {
                    'class':'form-control',
                    'id': 'hora_termino',
                    'type': 'time',
                }
            ),
            'dia': Select(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Dia',
                    'id': 'dia',
                }
            ),
            'color': HiddenInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Color',
                    'id': 'color',
                    'value': '1',
                }
            ),

        }

class CentroForm(ModelForm):
    class Meta:
        model = CentroDeportivo
        fields = ['nombre' , 'direccion', 'region', 'provincia', 'comuna']
        labels = {
            'nombre': 'Nombre del centro',
            'direccion': 'Direccion',
            'region': 'Region',
            'provincia': 'Provincia',
            'comuna': 'Comuna',
            }
        

    
  




    

  

    
    



  

