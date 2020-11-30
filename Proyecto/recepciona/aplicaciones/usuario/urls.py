
from django.urls import path
from .views import ListadoUsuario, EditarUsuario, EliminarUsuario, RegistrarUsuario, MiPerfil , EditarPerfil , ListadoCentro, ActualizarCentro, RegistroUsuario
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
path('listar_usuario/',login_required(ListadoUsuario.as_view()),name='listar_usuarios'),
path('inicio_usuarios/',login_required(TemplateView.as_view(template_name='usuarios/listar_usuario.html')),name='inicio_usuarios'),
path('actualizar_usuario/<int:pk>/',login_required(EditarUsuario.as_view()),name='actualizar_usuario'),
path('eliminar_usuario/<int:pk>/',login_required(EliminarUsuario.as_view()),name='eliminar_usuario'),
path('crear_usuario/',RegistrarUsuario.as_view(),name='crear_usuario'),
path('mi_perfil/',MiPerfil.as_view(),name='mi_perfil'),
path('actualizar_perfil/<int:pk>/',login_required(EditarPerfil.as_view()),name='actualizar_perfil'),
#este registro es a traves del home






#url de centro deportivo


path('mi_centro/',login_required(ListadoCentro.as_view()), name = 'mi_centro'),
path('inicio_centro/',login_required(TemplateView.as_view(template_name='usuarios/listar_centro.html')),name='inicio_centro'),
path('actualizar_centro/<int:pk>/',login_required(ActualizarCentro.as_view()),name='actualizar_centro'),




]
