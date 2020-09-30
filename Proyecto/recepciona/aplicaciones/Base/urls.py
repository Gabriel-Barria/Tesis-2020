from django.urls import path
from .views import CrearServicio, ListadoServicio, ActualizarServicio, EliminarServicio, crearCancha, crearSuperficie, crearHorario, crearCentro, crearTipo

urlpatterns = [
    path('Servicio/crear_servicio/',CrearServicio.as_view(), name = 'crear_servicio'),
    path('Servicio/listar_servicio/',ListadoServicio.as_view(), name = 'listar_servicio'),
    path('Servicio/editar_servicio/<int:pk>',ActualizarServicio.as_view(), name = 'editar_servicio'),
    path('Servicio/eliminar_servicio/<int:pk>',EliminarServicio.as_view(), name = 'eliminar_servicio'), 
    path('Cancha/crear_cancha/',crearCancha, name = 'crear_cancha'),
    path('Cancha/listar_cancha/',crearCancha, name = 'listar_cancha'),
    path('crear_superficie/',crearSuperficie, name = 'crear_superficie'),
    path('crear_horario/',crearHorario, name = 'crear_horario'),
    path('crear_centro/',crearCentro, name = 'crear_centro'),
    path('crear_tipo/',crearTipo, name = 'crear_tipo')
]

