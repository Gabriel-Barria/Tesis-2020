from django import forms
from django.contrib import admin
from django.forms import *
from .models import Servicio, Superficie, Cancha, Tipo_cancha, Horario, Reserva, Imagenes

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
        fields = ['nombre','imagen']
class CanchaForm(ModelForm):
    class Meta:
        model = Cancha
        fields = ['usuario','nombre','descripcion','valor','servicios','tipo_cancha','superficie','imagen']
        labels = {
            'nombre': 'Nombre de cancha',
            'descripcion': 'Descripcion',
            'valor':'Valor hora $$',
            'servicios': 'Servicios',
            'tipo_cancha':'Tipo de cancha',
            'superficie': 'Superficie',
            

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
        'servicios': CheckboxSelectMultiple(
                attrs = {
                    
                    
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
        fields = ['title','hora_inicio','hora_termino','dia']
        widgets = {
            'title': HiddenInput(
                attrs = {
                    'id': 'title',
                    'value': 'Ocupado',
                }
            ),
            'hora_inicio': TimeInput(
                attrs = {
                    'class':'form-control',
                    'type':'time',
                }
            ),
            'hora_termino': TimeInput(
                attrs = {
                    'class':'form-control',
                    'type':'time',

                }
            ),
            'dia': Select(
                attrs = {
                    'class':'form-control',
                     
                    
                }
            ),
            

        }
class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'cancha', 'date_start', 'date_end']
class ReservaFormCliente(ModelForm):

    class Meta:
        model = Reserva
        fields = ['usuario', 'cancha', 'date_start', 'date_end']
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
            
            
            

        }
class ImagenForm(ModelForm):
        class Meta:
            model = Imagenes
            fields = ['titulo','imagen']
            labels = {
                'titulo': 'Titulo de imagen',
                'imagen': 'Imagen',
                     }
            widgets = {
                'titulo': TextInput(
                    attrs = {
                        'class':'form-control',
                        'placeholder': 'Ingrese titulo',
                        
                }),
                'imagen': FileInput (
                    attrs = {
                        'class':'form-control',
                        'id': 'nombre',
                }),
            }
        
       
        

    
        
          




  




    

  

    
    



  

