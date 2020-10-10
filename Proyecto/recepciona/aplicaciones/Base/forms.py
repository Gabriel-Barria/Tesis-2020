from django import forms
from .models import Servicio, Superficie, cancha, Horario, CentroDeportivo, Tipo_cancha, Provincias, Regiones, Comunas
from django.contrib import admin

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre del servicio',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese nombre',
                    'id': 'nombre',
            })
        }

class SuperficieForm(forms.ModelForm):
    class Meta:
        model = Superficie
        fields = ['nombre']

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo_cancha
        fields = ['nombre']

class CanchaForm(forms.ModelForm):
    class Meta:
        model = cancha
        fields = ['nombre','descripcion','direccion','valor','servicios','tipo_cancha','superfice','centro_dep']

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['cancha','hora_inicio','hora_termino','dia']

class CentroForm(forms.ModelForm):
    class Meta:
        model = CentroDeportivo
        fields = ['Nombre' , 'direccion', 'region', 'provincia', 'comuna']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['provincia'].queryset = Provincias.objects.none()
        self.fields['comuna'].queryset = Comunas.objects.none()

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['provincia'].queryset = Provincias.objects.filter(region_id=region_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['provincia'].queryset = Provincias.objects.filter(self.instance.region)
        
        if 'provincia' in self.data:
            try:
                provincia_id = int(self.data.get('provincia'))
                self.fields['comuna'].queryset = Comunas.objects.filter(provincia_id=provincia_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['comuna'].queryset = Comunas.objects.filter(self.instance.provincia)

    
    



  

