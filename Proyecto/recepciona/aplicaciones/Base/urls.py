from django.urls import path
from .views import crearServicio, ListadoServicio, crearCancha, crearSuperficie, crearHorario, crearCentro, crearTipo


urlpatterns = [
    path('crear_servicio/',crearServicio, name = 'crear_servicio'),
    path('listar_servicio/',ListadoServicio.as_view(), name = 'listar_servicio'),
    path('crear_cancha/',crearCancha, name = 'crear_cancha'),
    path('crear_superficie/',crearSuperficie, name = 'crear_superficie'),
    path('crear_horario/',crearHorario, name = 'crear_horario'),
    path('crear_centro/',crearCentro, name = 'crear_centro'),
    path('crear_tipo/',crearTipo, name = 'crear_tipo')
]

