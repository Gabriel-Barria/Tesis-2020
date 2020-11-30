from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario, Centro

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
        fields = ('email', 'username','nombres','apellidos','role')
        labels = {
            'email': 'Email',
            'username': 'Nombre de usuario',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'role': 'Role',
            

            
            
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
                'placeholder':'Ingrese nombres',
            }
        ),
            'apellidos': TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Ingrese apellidos',
            }
        ),
            'role': Select(
                attrs={
                'class': 'form-control',
                'placeholder':'Role',
            }
        ),  
             
        
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
class EditarPerfilForms(ModelForm):

    class Meta:
        model = Usuario
        fields = ('email', 'username','nombres','apellidos','direccion','region','provincia','comuna','imagen')
        labels = {
            'email': 'Email',
            'username': 'Nombre de usuario',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'region': 'Region',
            'provincia':'Provincia',
            'comuna':'Comuna',
            'imagen':'Imagen'

            
            
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
                'placeholder':'Ingrese nombres',
            }
        ),
            'apellidos': TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Ingrese apellidos',
            }
        ),
            'direccion': TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Ingrese su dirección',
            }
        ),
            'region': Select(
                attrs={
                'class': 'form-control',
                
            }
        ),  
        'provincia': Select(
                attrs={
                'class': 'form-control',
                
            }
        ),
        'comuna': Select(
                attrs={
                'class': 'form-control',
                
            }
        ),
            
        
        }
class CentroForm(ModelForm):
    class Meta:
        model = Centro
        fields = ['nombre','descripcion','imagen_portada','logo','direccion', 'region', 'provincia', 'comuna']
        labels = {
            
            'nombre': 'Nombre del centro',
            'descripcion': 'Descripcion',
            'imagen_portada': 'Imagen de portada',
            'logo': 'Logo del centro',
            'direccion': 'Direccion',
            'region': 'Region',
            'provincia': 'Provincia',
            'comuna': 'Comuna',
            }
        widgets = {
            
            'nombre': TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Nombre de centro',
                    'id': 'nombre',
                }
            ),
            'descripcion': TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Descripcion',
                    'id': 'descripcion',
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
            'imagen_portada': FileInput(
                attrs = {
                    'class':'form-control-file',
                    
                    
                }
            ),
            'logo': FileInput(
                attrs = {
                   'class':'form-control-file', 
                }
            ),
        }
class FormUser(ModelForm):

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
        fields = ('email', 'username','nombres','apellidos','usuario_administrador','direccion','region','provincia','comuna')
        labels = {
            'email': 'Email',
            'username': 'Nombre de usuario',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'direccion':'Direccion',
            'region':'Region',
            'provinicia':'Provincia',
            'comuna':'Comuna',
            

            
            
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
                'placeholder':'Ingrese nombres',
            }
        ),
            'apellidos': TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Ingrese apellidos',
            }
        ),
            'usuario_administrador': HiddenInput(
                attrs={
                'value':'False'
                
            }
        ), 
            'direccion': TextInput(
                attrs={
                'class': 'form-control',
                'placeholder':'Ingrese su direccion',
                
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





    