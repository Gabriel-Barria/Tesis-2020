from django import forms
from .models import Servicio, Superficie, cancha, Horario, CentroDeportivo, Tipo_cancha, Provincias

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

