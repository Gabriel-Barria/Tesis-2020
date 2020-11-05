from django import forms
from django.contrib.auth.forms import AuthenticationForm
from aplicaciones.usuario.models import Usuario
from django.forms import *
class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUsuario(ModelForm):

    password1 = CharField(label = 'Contraseña', 
    widget = PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese contraseña',
            'id':'password1',
            'required':'required',
        }

    ))
    password2 = CharField(label = 'Contraseña', widget = PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Repita contraseña',
            'id':'password2',
            'required':'required',
        }

    ))
    class Meta:
        model = Usuario
        fields = ('email', 'username', 'nombres','apellidos', 'usuario_administrador' )
        labels = {
            'email': 'Email',
            'username': 'Nombre de usuario',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'usuario_administrador': '¿Usuario empresa?'
            
            }
        widgets = {
            'email': EmailInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Correo Electronico',
            }
        ),   
            'username': TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Nombre de usuario',
            }
        ),       
            'nombres': TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Nombres',
            }
        ),       
            'apellidos': TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Apellidos',
            }
        ),
            'usuario_administrador': CheckboxInput(
                attrs={
                }
        )
        }
    def clean_password2(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    