from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import CrearServicio, ListadoServicio, ActualizarServicio, EliminarServicio, CrearCancha, ListadoCancha, ActualizarCancha, EliminarCancha, CrearSuperficie, ListadoSuperficie, ActualizarSuperficie, EliminarSuperficie, CrearHorario, ListadoHorario, ActualizarHorario, EliminarHorario, CrearTipo, ListadoTipo, ActualizarTipo, EliminarTipo, CrearReserva, ListadoReservas, ActualizarReserva, EliminarReserva,  Descripcion_cancha, MisReservas
from . import views
urlpatterns = [
    path('Servicio/crear_servicio/',login_required(CrearServicio.as_view()), name = 'crear_servicio'),
    path('Servicio/listar_servicio/',login_required(ListadoServicio.as_view()), name = 'listar_servicio'),
    path('inicio_servicios/',login_required(TemplateView.as_view(template_name='Base/Servicio/listar_servicio.html')),name='inicio_servicio'),
    path('actualizar_servicio/<int:pk>/',login_required(ActualizarServicio.as_view()), name = 'actualizar_servicio'),
    path('eliminar_servicio/<int:pk>/',login_required(EliminarServicio.as_view()), name = 'eliminar_servicio'),
    #CRUD CANCHA 
    path('Cancha/crear_cancha/',login_required(CrearCancha.as_view()), name = 'crear_cancha'),
    path('Cancha/listar_cancha/',login_required(ListadoCancha.as_view()), name = 'listar_cancha'),
    path('inicio_canchas/',login_required(TemplateView.as_view(template_name='Base/Cancha/listar_cancha.html')),name='inicio_cancha'),
    path('actualizar_cancha/<int:pk>/',login_required(ActualizarCancha.as_view()), name = 'actualizar_cancha'),
    path('eliminar_cancha/<int:pk>/',login_required(EliminarCancha.as_view()), name = 'eliminar_cancha'),
    #CRUD SUPERFICIE
    path('Superficie/crear_superficie/',login_required(CrearSuperficie.as_view()), name = 'crear_superficie'),
    path('Superficie/listar_superficie/',login_required(ListadoSuperficie.as_view()), name = 'listar_superficie'),
    path('inicio_superficies/',login_required(TemplateView.as_view(template_name='Base/Superficie/listar_superficie.html')),name='inicio_superficie'),
    path('actualizar_superficie/<int:pk>/',login_required(ActualizarSuperficie.as_view()), name = 'actualizar_superficie'),
    path('eliminar_superficie/<int:pk>/',login_required(EliminarSuperficie.as_view()), name = 'eliminar_superficie'), 
    #CRUD HORARIO
    path('Horario/crear_horario/',login_required(CrearHorario.as_view()), name = 'crear_horario'),
    path('Horario/listar_horario/',login_required(ListadoHorario.as_view()), name = 'listar_horario'),
    path('inicio_horarios/',login_required(TemplateView.as_view(template_name='Base/Horario/listar_horario.html')),name='inicio_horario'),
    path('actualizar_horarios/<int:pk>/',login_required(ActualizarHorario.as_view()),name= 'actualizar_horario'),
    path('eliminar_horario/<int:pk>/',login_required(EliminarHorario.as_view()),name= 'eliminar_horario'),
      
   
    #CRUD TIPO
    path('Tipo_Cancha/crear_tipo/',login_required(CrearTipo.as_view()), name = 'crear_tipo'),
    path('Tipo_Cancha/listar_tipo/',login_required(ListadoTipo.as_view()), name = 'listar_tipo'),
    path('inicio_tipo/',login_required(TemplateView.as_view(template_name='Base/Tipo_Cancha/listar_tipo.html')),name='inicio_tipo'),
    path('actualizar_tipo/<int:pk>/',login_required(ActualizarTipo.as_view()), name = 'actualizar_tipo'),
    path('eliminar_tipo/<int:pk>/',login_required(EliminarTipo.as_view()), name = 'eliminar_tipo'),

    #CRUD RESERVA
    path('Reserva/crear_reserva/',login_required(CrearReserva.as_view()), name = 'crear_reserva'),
    path('Reserva/listar_reserva/',login_required(ListadoReservas.as_view()), name = 'listar_reserva'),
    path('inicio_reserva/',login_required(TemplateView.as_view(template_name='Base/Reserva/listar_reserva.html')),name='inicio_reserva'),
    path('actualizar_reserva/<int:pk>/',login_required(ActualizarReserva.as_view()), name = 'actualizar_reserva'),
    path('eliminar_reserva/<int:pk>/',login_required(EliminarReserva.as_view()), name = 'eliminar_reserva'),
    


    
    
    

]

