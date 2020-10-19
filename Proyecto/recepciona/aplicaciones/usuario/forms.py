from django import forms
from django.contrib.auth.forms import AuthenticationForm
from aplicaciones.usuario.models import Usuario
class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUsuario(forms.ModelForm):

    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese contraseña',
            'id':'password1',
            'required':'required',
        }

    ))
    password2 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Repita contraseña',
            'id':'password2',
            'required':'required',
        }

    ))
    class Meta:
        model = Usuario
        fields = ('email', 'username', 'nombres','apellidos')
        widget = {
            'email': forms.EmailInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Correo Electronico',
            }
        ),   
            'username': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Nombre de usuario',
            }
        ),       
            'nombres': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Nombres',
            }
        ),       
            'apellidos': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Apellidos',
            }
        )
        }
