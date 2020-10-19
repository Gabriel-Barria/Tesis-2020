from django.urls import path
from aplicaciones.usuario.views import ListadoUsuario,RegistrarUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
path('listado_usuarios/',login_required(ListadoUsuario.as_view()),name='listar_usuarios'),
path('registrar_usuarios/',login_required(RegistrarUsuario.as_view()),name='registrar_usuario'),
]