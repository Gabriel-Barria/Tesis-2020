from django.shortcuts import render, redirect
from .forms import ServicioForm, SuperficieForm, CentroForm, HorarioForm, CanchaForm, TipoForm
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import Servicio, Superficie, CentroDeportivo, Horario, cancha, Tipo_cancha, Regiones, Provincias, Comunas
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 


#Vistas basadas en clases: CRUD Servicio

class Inicio(TemplateView):
    template_name = 'index.html'

class ListadoServicio(ListView):
    model = Servicio
    template_name = 'Base/Servicio/listar_servicio.html'
    queryset = Servicio.objects.filter(estado=True)
class ActualizarServicio(UpdateView):
    model = Servicio
    template_name = 'Base/Servicio/crear_servicio.html'
    form_class = ServicioForm
    success_url = reverse_lazy('Base:listar_servicio')
class CrearServicio(CreateView):
    model = Servicio
    template_name = 'Base/Servicio/crear_servicio.html'
    form_class = ServicioForm
    success_url = reverse_lazy('Base:listar_servicio')
class EliminarServicio(DeleteView):
    model = Servicio    

    def post(self, request, pk, *args, **kwargs):
        object = Servicio.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('Base:listar_servicio')
#Vistas basadas en clases: CRUD Superficie

class ListadoSuperficie(ListView):
    model = Superficie
    template_name = 'Base/Superficie/listar_superficie.html'
    queryset = Superficie.objects.filter(estado=True)

class ActualizarSuperficie(UpdateView):
    model = Superficie
    template_name = 'Base/Superficie/crear_superficie.html'
    form_class = SuperficieForm
    success_url = reverse_lazy('Base:listar_superficie')

class CrearSuperficie(CreateView):
    model = Superficie
    template_name = 'Base/Superficie/crear_superficie.html'
    form_class = SuperficieForm
    success_url = reverse_lazy('Base:listar_superficie')

    
        
    

class EliminarSuperficie(DeleteView):
    model = Superficie   

    def post(self, request, pk, *args, **kwargs):
        object = Superficie.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('Base:listar_superficie')

#CRUD Centro deportivo:

class ListadoCentro(ListView):
    model = CentroDeportivo
    template_name = 'Base/Centro_deportivo/listar_centro.html'
    queryset = CentroDeportivo.objects.filter(estado=True)

class ActualizarCentro(UpdateView):
    model = CentroDeportivo
    template_name = 'Base/Centro_deportivo/crear_centro.html'
    form_class = CentroForm
    success_url = reverse_lazy('Base:listar_centro')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')

        context = super(ActualizarCentro, self).get_context_data(**kwargs)
        context["region"] = Regiones.objects.all()  
        context["provincia"] = Provincias.objects.all()
        context["comuna"] = Comunas.objects.all()
        context["obj"] = CentroDeportivo.objects.filter(pk=pk).first()
        return context

class CrearCentro(CreateView):
    model = CentroDeportivo
    template_name = 'Base/Centro_deportivo/crear_centro.html'
    form_class = CentroForm
    success_url = reverse_lazy('Base:listar_centro')
    def get_context_data(self, **kwargs):
        context = super(CrearCentro, self).get_context_data(**kwargs)
        context["region"] = Regiones.objects.all()  
        context["provincia"] = Provincias.objects.all()
        context["comuna"] = Comunas.objects.all()
        return context
class EliminarCentro(DeleteView):
    model = CentroDeportivo  

    def post(self, request, pk, *args, **kwargs):
        object = CentroDeportivo.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('Base:listar_centro')

#CRUD Horario 

class ListadoHorario(ListView):
    model = Horario
    template_name = 'Base/Horario/listar_horario.html'
    queryset = Horario.objects.filter(estado=True)

class ActualizarHorario(UpdateView):
    model = Horario
    template_name = 'Base/Horario/listar_horario.html'
    form_class = HorarioForm
    success_url = reverse_lazy('Base:listar_horario')

    

class CrearHorario(CreateView):
    model = Horario
    template_name = 'Base/Horario/crear_horario.html'
    form_class = HorarioForm
    success_url = reverse_lazy('Base:listar_horario')

class EliminarHorario(DeleteView):
    model = Horario  

    def post(self, request, pk, *args, **kwargs):
        object = Horario.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('Base:listar_horario')

#CRUD Cancha
class ListadoCancha(ListView):
    model = cancha
    template_name = 'Base/Cancha/listar_cancha.html'
    queryset = cancha.objects.filter(estado=True)

class ActualizarCancha(UpdateView):
    model = cancha
    template_name = 'Base/Cancha/crear_cancha.html'
    form_class = CanchaForm
    success_url = reverse_lazy('Base:listar_cancha')

class CrearCancha(CreateView):
    model = cancha
    template_name = 'Base/Cancha/crear_cancha.html'
    form_class = CanchaForm
    success_url = reverse_lazy('Base:listar_cancha')

class EliminarCancha(DeleteView):
    model = cancha

    def post(self, request, pk, *args, **kwargs):
        object = cancha.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('Base:listar_cancha')

#CRUD Tipo

class ListadoTipo(ListView):
    model = Tipo_cancha
    template_name = 'Base/Tipo_Cancha/listar_tipo.html'
    queryset = Tipo_cancha.objects.filter(estado=True)

class ActualizarTipo(UpdateView):
    model = Tipo_cancha
    template_name = 'Base/Tipo_Cancha/listar_tipo.html'
    form_class = TipoForm
    success_url = reverse_lazy('Base:listar_tipo')

class CrearTipo(CreateView):
    model = Tipo_cancha
    template_name = 'Base/Tipo_Cancha/crear_tipo.html'
    form_class = TipoForm
    success_url = reverse_lazy('Base:listar_tipo')

class EliminarTipo(DeleteView):
    model = Tipo_cancha 

    def post(self, request, pk, *args, **kwargs):
        object = Tipo_cancha.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('Base:listar_tipo')