from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import CrearServicio, ListadoServicio, ActualizarServicio, EliminarServicio, CrearCancha, ListadoCancha, ActualizarCancha, EliminarCancha, CrearSuperficie, ListadoSuperficie, ActualizarSuperficie, EliminarSuperficie, CrearHorario, ListadoHorario, ActualizarHorario, EliminarHorario, CrearCentro, ListadoCentro, ActualizarCentro, EliminarCentro, CrearTipo, ListadoTipo, ActualizarTipo, EliminarTipo, Descripcion_cancha
from . import views
urlpatterns = [
    path('Servicio/crear_servicio/',login_required(CrearServicio.as_view()), name = 'crear_servicio'),
    path('Servicio/listar_servicio/',login_required(ListadoServicio.as_view()), name = 'listar_servicio'),
    path('Servicio/editar_servicio/<int:pk>',login_required(ActualizarServicio.as_view()), name = 'editar_servicio'),
    path('Servicio/eliminar_servicio/<int:pk>',login_required(EliminarServicio.as_view()), name = 'eliminar_servicio'),
    #CRUD CANCHA 
    path('Cancha/crear_cancha/',CrearCancha.as_view(), name = 'crear_cancha'),
    path('Cancha/listar_cancha/',ListadoCancha.as_view(), name = 'listar_cancha'),
    path('Cancha/editar_cancha/<int:pk>',ActualizarCancha.as_view(), name = 'editar_cancha'),
    path('Cancha/eliminar_cancha/<int:pk>',EliminarCancha.as_view(), name = 'eliminar_cancha'),
    #CRUD SUPERFICIE
    path('Superficie/crear_superficie/',CrearSuperficie.as_view(), name = 'crear_superficie'),
    path('Superficie/listar_superficie/',ListadoSuperficie.as_view(), name = 'listar_superficie'),
    path('Superficie/editar_superficie/<int:pk>',ActualizarSuperficie.as_view(), name = 'editar_superficie'),
    path('Superficie/eliminar_superficie/<int:pk>',EliminarSuperficie.as_view(), name = 'eliminar_superficie'), 
    #CRUD HORARIO
    path('Horario/crear_horario/',CrearHorario.as_view(), name = 'crear_horario'),
    path('Horario/listar_horario/',ListadoHorario.as_view(), name = 'listar_horario'),
    path('Horario/editar_horario/<int:pk>',ActualizarHorario.as_view(), name = 'editar_horario'),
    path('Horario/eliminar_horario/<int:pk>',EliminarHorario.as_view(), name = 'eliminar_horario'),
    #CRUD CENTRO
    path('Centro_deportivo/crear_centro/',CrearCentro.as_view(), name = 'crear_centro'),
    path('Centro_deportivo/listar_centro/',ListadoCentro.as_view(), name = 'listar_centro'),
    path('Centro_deportivo/editar_centro/<int:pk>',ActualizarCentro.as_view(), name = 'editar_centro'),
    path('Centro_deportivo/eliminar_centro/<int:pk>',EliminarCentro.as_view(), name = 'eliminar_centro'),   
   
    #CRUD TIPO
    path('Tipo_Cancha/crear_tipo/',CrearTipo.as_view(), name = 'crear_tipo'),
    path('Tipo_Cancha/listar_tipo/',ListadoTipo.as_view(), name = 'listar_tipo'),
    path('Tipo_Cancha/editar_tipo/<int:pk>',ActualizarTipo.as_view(), name = 'editar_tipo'),
    path('Tipo_Cancha/eliminar_tipo/<int:pk>',EliminarTipo.as_view(), name = 'eliminar_tipo'),

    path('Descripcion_cancha.html',Descripcion_cancha.as_view(), name = 'Descripcion_cancha'),

]

