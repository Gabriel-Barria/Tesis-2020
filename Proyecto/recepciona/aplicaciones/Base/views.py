from django.shortcuts import render, redirect
from .forms import ServicioForm, SuperficieForm, CentroForm, HorarioForm, CanchaForm, TipoForm, ReservaForm, ReservaFormCliente
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Servicio, Superficie, CentroDeportivo, Horario, Cancha, Tipo_cancha, Regiones, Provincias, Comunas, Imagenes, Reserva
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from django.core.serializers import serialize
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Q
#Vistas basadas en clases: CRUD Servicio

class Inicio(TemplateView):
    template_name = 'index.html'

def home(request):
    q = request.GET.get("buscar_tipo")    
    Canchas = Cancha.objects.all()
    
    tipo_cancha = Tipo_cancha.objects.all()
    
    if q:
        Canchas = Cancha.objects.filter(
            tipo_cancha__id = q  
            
        )
           
    
    context = {
        'Canchas':Canchas,        
        'tipo_cancha': tipo_cancha,
    }

    return render(request,'home.html',context)
        
        


class Descripcion_cancha(View):
    template_name = 'Descripcion_cancha.html'
    form_class = ReservaFormCliente
    model = Reserva

    def recuperar_pk(self,**kwargs):
        pk = self.kwargs.get('pk')
        return pk
    def get_context_data(self,**kwargs):
         
         pk = self.kwargs.get('pk')
         context = {}
         context['Cancha'] = Cancha.objects.get(pk=pk)
         context['Imagenes'] = Imagenes.objects.filter(cancha_id=pk)
         context['Horario'] = Horario.objects.filter(cancha=pk)
         context['Reserva'] = Reserva.objects.filter(cancha=pk)
         context['form'] = self.form_class
        
         return context
   
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())

    def post(self, request, *args,**kwargs):
        pk = self.kwargs.get('pk')
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('Descripcion_cancha', pk)
       
        else: 
            return redirect('home')    
     
    
 


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

class ListadoCentro(View):
    model = CentroDeportivo
    form_class = CentroForm
    template_name = 'Base/Centro_deportivo/listar_centro.html'
    
    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['centros'] = self.get_queryset()
        contexto['form'] = self.form_class
        
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())

    


class ActualizarCentro(UpdateView):
    model = CentroDeportivo
    template_name = 'Base/Centro_deportivo/centro.html'
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
    template_name = 'Base/Horario/crear_horario.html'
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



class ListadoCancha(View):
    model = Cancha
    form_class = CanchaForm
    template_name = 'Base/Cancha/listar_cancha.html'
    
    
    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['canchas'] = self.get_queryset()
        contexto['form'] = self.form_class
        
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())

class ActualizarCancha(UpdateView):
    model = Cancha
    template_name = 'Base/Cancha/cancha.html'
    form_class = CanchaForm
    success_url = reverse_lazy('Base:listar_cancha')

class CrearCancha(CreateView):
    model = Cancha
    template_name = 'Base/Cancha/crear_cancha.html'
    form_class = CanchaForm
    success_url = reverse_lazy('Base:listar_cancha')

    


class EliminarCancha(DeleteView):
    model = Cancha
    form_class = CanchaForm
    success_url = reverse_lazy('Base:listar_cancha')

    

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

#CRUD DE RESERVAS

class ListadoReservas(ListView):
    model = Reserva
    template_name = 'Base/Reserva/listar_reserva.html'
    queryset = Reserva.objects.filter(estado=True)

class ActualizarReserva(UpdateView):
    model = Reserva
    template_name = 'Base/Reserva/crear_reserva.html'
    form_class = ReservaForm
    success_url = reverse_lazy('Base:listar_reserva')

class CrearReserva(CreateView):
    model = Reserva
    template_name = 'Base/Reserva/crear_reserva.html'
    form_class = ReservaForm
    success_url = reverse_lazy('Base:listar_reserva')
class CrearReservaCliente(CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy('Base:listar_reserva')


class EliminarReserva(DeleteView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy('Base:listar_reserva')

    
class MisReservas(View):
    template_name = 'mis_reservas.html'
    model = Reserva

    def get_context_data(self,**kwargs):
         
         pk = self.kwargs.get('pk')
         context = {}
         context['reserva'] = Reserva.objects.filter(usuario=pk)
         return context

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())

