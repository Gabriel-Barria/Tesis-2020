from django.urls import path
from aplicaciones.usuario.views import ListadoUsuario,RegistrarUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
path('listar_usuario/',ListadoUsuario.as_view(),name='listar_usuarios'),
path('registrar_usuario/',RegistrarUsuario.as_view(),name='registrar_usuario'),
]