from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import CrearServicio, ListadoServicio, ActualizarServicio, EliminarServicio, CrearCancha, ListadoCancha, ActualizarCancha, EliminarCancha, CrearSuperficie, ListadoSuperficie, ActualizarSuperficie, EliminarSuperficie, CrearHorario, ListadoHorario, ActualizarHorario, EliminarHorario, CrearCentro, ListadoCentro, ActualizarCentro, EliminarCentro, CrearTipo, ListadoTipo, ActualizarTipo, EliminarTipo, CrearReserva, ListadoReservas, ActualizarReserva, EliminarReserva,  Descripcion_cancha, MisReservas
from . import views
urlpatterns = [
    path('Servicio/crear_servicio/',login_required(CrearServicio.as_view()), name = 'crear_servicio'),
    path('Servicio/listar_servicio/',login_required(ListadoServicio.as_view()), name = 'listar_servicio'),
    path('Servicio/editar_servicio/<int:pk>',login_required(ActualizarServicio.as_view()), name = 'editar_servicio'),
    path('Servicio/eliminar_servicio/<int:pk>',login_required(EliminarServicio.as_view()), name = 'eliminar_servicio'),
    #CRUD CANCHA 
    
    path('Cancha/crear_cancha/',login_required(CrearCancha.as_view()), name = 'crear_cancha'),
    path('Cancha/listar_cancha/',login_required(ListadoCancha.as_view()), name = 'listar_cancha'),
    path('Cancha/editar_cancha/<int:pk>',login_required(ActualizarCancha.as_view()), name = 'editar_cancha'),
    path('Cancha/eliminar_cancha/<int:pk>',login_required(EliminarCancha.as_view()), name = 'eliminar_cancha'),
    #CRUD SUPERFICIE
    path('Superficie/crear_superficie/',login_required(CrearSuperficie.as_view()), name = 'crear_superficie'),
    path('Superficie/listar_superficie/',login_required(ListadoSuperficie.as_view()), name = 'listar_superficie'),
    path('Superficie/editar_superficie/<int:pk>',login_required(ActualizarSuperficie.as_view()), name = 'editar_superficie'),
    path('Superficie/eliminar_superficie/<int:pk>',login_required(EliminarSuperficie.as_view()), name = 'eliminar_superficie'), 
    #CRUD HORARIO
    path('Horario/crear_horario/',login_required(CrearHorario.as_view()), name = 'crear_horario'),
    path('Horario/listar_horario/',login_required(ListadoHorario.as_view()), name = 'listar_horario'),
    path('Horario/editar_horario/<int:pk>',login_required(ActualizarHorario.as_view()), name = 'editar_horario'),
    path('Horario/eliminar_horario/<int:pk>',login_required(EliminarHorario.as_view()), name = 'eliminar_horario'),
    #CRUD CENTRO
    path('Centro_deportivo/crear_centro/',login_required(CrearCentro.as_view()), name = 'crear_centro'),
    path('Centro_deportivo/listar_centro/',login_required(ListadoCentro.as_view()), name = 'listar_centro'),
    path('Centro_deportivo/editar_centro/<int:pk>',login_required(ActualizarCentro.as_view()), name = 'editar_centro'),
    path('Centro_deportivo/eliminar_centro/<int:pk>',login_required(EliminarCentro.as_view()), name = 'eliminar_centro'),   
   
    #CRUD TIPO
    path('Tipo_Cancha/crear_tipo/',login_required(CrearTipo.as_view()), name = 'crear_tipo'),
    path('Tipo_Cancha/listar_tipo/',login_required(ListadoTipo.as_view()), name = 'listar_tipo'),
    path('Tipo_Cancha/editar_tipo/<int:pk>',login_required(ActualizarTipo.as_view()), name = 'editar_tipo'),
    path('Tipo_Cancha/eliminar_tipo/<int:pk>',login_required(EliminarTipo.as_view()), name = 'eliminar_tipo'),

    #CRUD RESERVA
    path('Reserva/crear_reserva/',login_required(CrearReserva.as_view()), name = 'crear_reserva'),
    path('Reserva/listar_reserva/',login_required(ListadoReservas.as_view()), name = 'listar_reserva'),
    path('Reserva/editar_reserva/<int:pk>',login_required(ActualizarReserva.as_view()), name = 'editar_reserva'),
    path('Reserva/eliminar_reserva/<int:pk>',login_required(EliminarReserva.as_view()), name = 'eliminar_reserva'),
    


    
    
    

]

