from django.shortcuts import render, redirect
from .forms import ServicioForm, SuperficieForm, CentroForm, HorarioForm, CanchaForm, TipoForm
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import Servicio
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy

#Create your views here.

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

def crearSuperficie(request):
    if request.method == 'POST':
        superficie_form = SuperficieForm(request.POST)
        if superficie_form.is_valid():
            superficie_form.save()
            return redirect('index')
    else:
        superficie_form = SuperficieForm()
    return render(request,'Base/Superficie/crear_servicio.html',{'servicio_form':superficie_form})

def crearCentro(request):
    if request.method == 'POST':
        centro_form = CentroForm(request.POST)
        if centro_form.is_valid():
            centro_form.save()
            return redirect('index')
    else:
        centro_form = CentroForm()
    return render(request,'Base/Centro_deportivo/crear_centro.html',{'centro_form':centro_form})

def crearHorario(request):
    if request.method == 'POST':
        horario_form = HorarioForm(request.POST)
        if horario_form.is_valid():
            horario_form.save()
            return redirect('index')
    else:
        horario_form = HorarioForm()
    return render(request,'Base/Horario/crear_horario.html',{'horario_form':horario_form})

def crearCancha(request):
    if request.method == 'POST':
        cancha_form = CanchaForm(request.POST)
        if cancha_form.is_valid():
            cancha_form.save()
            return redirect('index')
    else:
        cancha_form = CanchaForm()
    return render(request,'Base/Cancha/crear_cancha.html',{'cancha_form':cancha_form})

def crearTipo(request):
    if request.method == 'POST':
        tipo_form = TipoForm(request.POST)
        if tipo_form.is_valid():
            tipo_form.save()
            return redirect('index')
    else:
        tipo_form = TipoForm()
    return render(request,'Base/Tipo_Cancha/crear_tipo.html',{'tipo_form':tipo_form})







