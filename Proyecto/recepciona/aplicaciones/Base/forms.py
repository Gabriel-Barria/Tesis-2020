from django import forms
from .models import Servicio, Superficie, Cancha, Horario, CentroDeportivo, Tipo_cancha, Provincias, Regiones, Comunas, Reserva
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
        labels = {
            'nombre': 'Nombre de cancha',
            'descripcion': 'Descripcion',
            'valor':'Valor hora',
            'servicios': 'Servicios',
            'tipo_cancha':'Tipo de cancha',
            'superficie': 'Superficie',
            'centro_dep': 'Centro deportivo',

        }
        widgets = {
            'usuario_id':HiddenInput(attrs={

            }
        ),
        'nombre':TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nombre de cancha',
            }
        ),
        'descripcion': Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Descripcion',
                    
                    
                }
            ),
        'valor': NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese valor hora',
                    
                }
            ),
        'servicios': SelectMultiple(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese servicios',
                    
                }
            ),
        
        'tipo_cancha': Select(
                attrs = {
                    'class':'form-control',
                    
                    
                }
            ),
        'superficie': Select(
                attrs = {
                    'class':'form-control',
                    
                    
                }
            ),
        'centro_dep': Select(
                attrs = {
                    'class':'form-control',
                    
                    
                }
            ),
        }
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
        fields = ['usuario_id','nombre' , 'direccion', 'region', 'provincia', 'comuna']
        labels = {
            'usuario_id': 'Nombre de usuario',
            'nombre': 'Nombre del centro',
            'direccion': 'Direccion',
            'region': 'Region',
            'provincia': 'Provincia',
            'comuna': 'Comuna',
            }
        widgets = {
            'usuario_id': HiddenInput(
                attrs = {
                    
                }
            ),

            'nombre': TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Nombre de centro',
                    'id': 'nombre',
                }
            ),
            'direccion': TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Direccion',
                    'id': 'direccion',
                }
            ),
            'region': Select(
                attrs = {
                    'class':'form-control',
                    'id': 'id_region',
                }
            ),
            'provincia': Select(
                attrs = {
                    'class':'form-control',
                    'id': 'id_provincia',
                }
            ),
            'comuna': Select(
                attrs = {
                    'class':'form-control',
                    'id': 'id_comuna',
                }
            ),
        }
class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'cancha', 'date_start', 'date_end', 'color']

class ReservaFormCliente(ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'cancha', 'date_start', 'date_end', 'color']
        labels = {
            
            'date_start': 'Desde',
            'date_end': 'Hasta',
            }

        widgets = {
            'usuario': HiddenInput(
                attrs = {
                 
                }
            ),
            'cancha': HiddenInput(
                attrs = {
                    
                }
            ),
            'date_start':TextInput(
                attrs = {
                    'readonly': 'true'
                    
                    
                }
            ),
            'date_end': TextInput(
                attrs = {                    
                   'readonly': 'true' 
                }
            ),
            
            'color': HiddenInput(
                attrs = {
                   
                }
            ),
            

        }
        
          
        
       
        

    
  




    

  

    
    



  

