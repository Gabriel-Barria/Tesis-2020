from django.shortcuts import render, redirect
from .forms import ServicioForm, SuperficieForm, HorarioForm, CanchaForm, TipoForm, ReservaForm, ReservaFormCliente, ImagenForm
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Servicio, Superficie,  Cancha, Tipo_cancha,  Imagenes, Horario, Reserva
from aplicaciones.usuario.models import Centro, Usuario
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from django.core.serializers import serialize
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

#Esta clase redirecciona al area de admnistracion del sitio
class Inicio(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
         pk = self.kwargs.get('pk')
         context = {}
         
         context['usuario'] = Usuario.objects.filter(usuario_administrador = False)
         context['reserva'] = Reserva.objects.filter(estado=True)
         context['reserva_false'] = Reserva.objects.filter(estado=False)
         context['cancha'] = Cancha.objects.filter(estado=True)
         
         return context
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())
class Inicio_home(ListView):
    template_name = 'home.html'
    model = Centro
    form_class = ReservaFormCliente

    def get_context_data(self,**kwargs):
         pk = self.kwargs.get('pk')
         context = {}
         context['centro'] = Centro.objects.all()
         context['imagen'] = Imagenes.objects.filter(estado=True)
         context['horario'] = Horario.objects.filter(estado=True)
         context['reserva'] = Reserva.objects.filter(cancha=pk, estado=True) 
         context['cancha'] = Cancha.objects.filter(pk=pk,estado=True)
         context['form'] = self.form_class      
        
         return context
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                    form.save()
                    mensaje = 'Reserva realizada con exito!' 
                    error = 'No hay error!'
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 201
                    return response
            else:
                    mensaje = 'No se ha podido registrar!' 
                    error = form.errors
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 400
                    return response
        else:
             return redirect('inicio_home')
class Home(View):
    template_name = 'home.html'
    model = Centro
    model2 = Tipo_cancha
    form_class = ReservaFormCliente
     

    def get_queryset(self):
        return self.model2.objects.filter(estado=True)

    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():           
            return HttpResponse(serialize('json',self.get_queryset()),'application/json')
        else:
            return redirect('inicio_home')       
class Filtro_cancha(View):
    template_name = 'home.html'
    model = Centro
    model2 = Tipo_cancha 

    def get(self,request,*args,**kwargs):
        r = self.kwargs.get('pk')
        cancha = Cancha.objects.filter(estado=True)        
        if request.is_ajax():
            if r:
                cancha = Cancha.objects.filter(tipo_cancha=r, estado=True)
                return HttpResponse(serialize('json',cancha),'application/json')

        else:
             return redirect('inicio_home')
class MostrarCalendario(View):
    template_name = 'calendario.html'
    form_class = ReservaFormCliente
    model = Reserva
    
   
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())
    def get_context_data(self,**kwargs):
         pk = self.kwargs.get('pk')
         context = {}
         context['horario'] = Horario.objects.filter(estado=True)
         context['reserva'] = Reserva.objects.filter(cancha=pk, estado=True) 
         context['cancha'] = Cancha.objects.filter(pk=pk,estado=True)
         context['form'] = self.form_class      
        
         return context
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                    form.save()
                    mensaje = 'Reserva realizada con exito!' 
                    error = 'No hay error!'
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 201
                    return response
            else:
                    mensaje = f'{self.model.__name__} No se ha podido registrar!' 
                    error = form.errors
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 400
                    return response
        else:
             return redirect('inicio_home')
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
         context['cancha'] = Cancha.objects.get(pk=pk)
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
#CRUD SERVICIO
class ListadoServicio(ListView):
    model = Servicio
    template_name = 'Base/Servicio/listar_servicio.html'

    def get_queryset(self):
        return self.model.objects.filter(estado=True)
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():
           
            return HttpResponse(serialize('json',self.get_queryset()),'application/json')
        else:
            return redirect('Base:inicio_servicio')
class ActualizarServicio(UpdateView):
    model = Servicio
    template_name = 'Base/Servicio/editar_servicio.html'
    form_class = ServicioForm
    
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
             return redirect('Base:inicio_servicio')
class CrearServicio(CreateView):
    model = Servicio
    template_name = 'Base/Servicio/crear_servicio.html'
    form_class = ServicioForm
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                    form.save()
                    mensaje = f'{self.model.__name__} registrado correctamente!' 
                    error = 'No hay error!'
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 201
                    return response
            else:
                    mensaje = f'{self.model.__name__} No se ha podido registrar!' 
                    error = form.errors
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 400
                    return response
        else:
             return redirect('Base:inicio_servicio')
class EliminarServicio(DeleteView):
    model = Servicio 
    template_name = 'Base/Servicio/eliminar_servicio.html'   

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            servicio = self.get_object()
            servicio.estado = False
            servicio.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Base:inicio_servicio')
#CRUD SUPERFICIE
class ListadoSuperficie(ListView):
    model = Superficie
    template_name = 'Base/Superficie/listar_superficie.html'
    

    def get_queryset(self):
        return self.model.objects.filter(estado=True)
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():
           
            return HttpResponse(serialize('json',self.get_queryset()),'application/json')
        else:
             return redirect('Base:inicio_superficie')
class ActualizarSuperficie(UpdateView):
    model = Superficie
    template_name = 'Base/Superficie/editar_superficie.html'
    form_class = SuperficieForm
    

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
             return redirect('Base:inicio_superficie')
class CrearSuperficie(CreateView):
    model = Superficie
    template_name = 'Base/Superficie/crear_superficie.html'
    form_class = SuperficieForm
    

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                    form.save()
                    mensaje = f'{self.model.__name__} registrado correctamente!' 
                    error = 'No hay error!'
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 201
                    return response
            else:
                    mensaje = f'{self.model.__name__} No se ha podido registrar!' 
                    error = form.errors
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 400
                    return response
        else:
             return redirect('Base:inicio_superficie')
class EliminarSuperficie(DeleteView):
    model = Superficie  
    template_name = 'Base/Superficie/eliminar_superficie.html' 

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            superficie = self.get_object()
            superficie.estado = False
            superficie.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Base:inicio_superficie')
#CRUD CANCHA
class ListadoCancha(View):
    model = Cancha    
    template_name = 'Base/Cancha/listar_cancha.html'
    
    
    def get_queryset(self):
        return self.model.objects.filter(estado=True)
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():
           
            return HttpResponse(serialize('json',self.get_queryset()),'application/json')
        else:
            return redirect('Base:inicio_cancha')
class ActualizarCancha(UpdateView):
    model = Cancha
    template_name = 'Base/Cancha/editar_cancha.html'
    form_class = CanchaForm
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('Base:inicio_cancha')
class CrearCancha(CreateView):
    model = Cancha
    template_name = 'Base/Cancha/crear_cancha.html'
    form_class = CanchaForm

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST, files = request.FILES)
            if form.is_valid():
                    form.save()
                    mensaje = f'{self.model.__name__} registrado correctamente!' 
                    error = 'No hay error!'
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 201
                    return response
            else:
                    mensaje = f'{self.model.__name__} No se ha podido registrar!' 
                    error = form.errors
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 400
                    return response
        else:
            return redirect('Base:inicio_cancha')
class EliminarCancha(DeleteView):
    model = Cancha
    form_class = CanchaForm
    template_name = 'Base/Cancha/eliminar_cancha.html'
    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            cancha = self.get_object()
            cancha.estado = False
            cancha.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Base:listar_cancha')
#CRUD RESERVA
class ListadoReservas(ListView):
    model = Reserva
    template_name = 'Base/Reserva/listar_reserva.html'
    def get_queryset(self):
        return self.model.objects.filter(estado=True)
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():
           
            return HttpResponse(serialize('json',self.get_queryset()),'application/json')
        else:
            return redirect('Base:inicio_reserva')
class ActualizarReserva(UpdateView):
    model = Reserva
    template_name = 'Base/Reserva/editar_reserva.html'
    form_class = ReservaForm
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
             return redirect('Base:inicio_reserva')
class CrearReserva(CreateView):
    model = Reserva
    template_name = 'Base/Reserva/crear_reserva.html'
    form_class = ReservaForm
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                    form.save()
                    mensaje = f'{self.model.__name__} registrado correctamente!' 
                    error = 'No hay error!'
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 201
                    return response
            else:
                    mensaje = f'{self.model.__name__} No se ha podido registrar!' 
                    error = form.errors
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 400
                    return response
        else:
             return redirect('Base:inicio_reserva')
class CrearReservaCliente(CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy('Base:listar_reserva')
class EliminarReserva(DeleteView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'Base/Reserva/eliminar_reserva.html'
    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            servicio = self.get_object()
            servicio.estado = False
            servicio.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Base:inicio_servicio')
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
#CRUD TIPO DE CANCHA
class ListadoTipo(ListView):
    model = Tipo_cancha
    template_name = 'Base/Tipo_Cancha/listar_tipo.html'
    def get_queryset(self):
        return self.model.objects.filter(estado=True)
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():
           
            return HttpResponse(serialize('json',self.get_queryset()),'application/json')
        else:
            return redirect('Base:inicio_tipo')
class ActualizarTipo(UpdateView):
    model = Tipo_cancha
    template_name = 'Base/Tipo_Cancha/editar_tipo.html'
    form_class = TipoForm
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
             return redirect('Base:inicio_tipo')
class CrearTipo(CreateView):
    model = Tipo_cancha
    template_name = 'Base/Tipo_Cancha/crear_tipo.html'
    form_class = TipoForm
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                    form.save()
                    mensaje = f'{self.model.__name__} registrado correctamente!' 
                    error = 'No hay error!'
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 201
                    return response
            else:
                    mensaje = f'{self.model.__name__} No se ha podido registrar!' 
                    error = form.errors
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 400
                    return response
        else:
             return redirect('Base:inicio_tipo')
class EliminarTipo(DeleteView):
    model = Tipo_cancha 
    template_name = 'Base/Tipo_Cancha/eliminar_tipo.html'

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            tipo = self.get_object()
            tipo.estado = False
            tipo.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Base:inicio_tipo')
#CRUD HORARIO
class ListadoHorario(ListView):
    model = Horario
    
    
    def get_queryset(self):
        return self.model.objects.filter(estado=True)
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():
           
            return HttpResponse(serialize('json',self.get_queryset()),'application/json')
        else:
            return redirect('Base:inicio_horario')
class ActualizarHorario(UpdateView):
    model = Horario
    template_name = 'Base/Horario/editar_horario.html'
    form_class = HorarioForm
    

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('Base:inicio_horario')
class CrearHorario(CreateView):
    model = Horario
    template_name = 'Base/Horario/crear_horario.html'
    form_class = HorarioForm
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                    form.save()
                    mensaje = f'{self.model.__name__} registrado correctamente!' 
                    error = 'No hay error!'
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 201
                    return response
            else:
                    mensaje = f'{self.model.__name__} No se ha podido registrar!' 
                    error = form.errors
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 400
                    return response
        else:
            return redirect('Base:inicio_horario')
class EliminarHorario(DeleteView):
    model = Horario 
    template_name = 'Base/Horario/eliminar_horario.html' 

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            horario = self.get_object()
            horario.estado = False
            horario.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Base:listar_horario')
#CRUD IMAGENES
class ListadoImagenes(ListView):
    model = Imagenes    
    
    def get_queryset(self):
        return self.model.objects.filter(estado=True)
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():
           
            return HttpResponse(serialize('json',self.get_queryset()),'application/json')
        else:
            return redirect('Base:inicio_imagen')
class ActualizarImagenes(UpdateView):
    model = Imagenes
    template_name = 'Base/Imagen/editar_imagen.html'
    form_class = ImagenForm
    
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('Base:inicio_imagen')
class CrearImagen(CreateView):
    model = Imagenes
    template_name = 'Base/Imagen/crear_imagen.html'
    form_class = ImagenForm
    

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,request.FILES)
            if form.is_valid():
                    form.save()
                    mensaje = f'{self.model.__name__} registrado correctamente!' 
                    error = 'No hay error!'
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 201
                    return response
            else:
                    mensaje = f'{self.model.__name__} No se ha podido registrar!' 
                    error = form.errors
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 400
                    return response
        else:
            return redirect('Base:inicio_imagen')
class EliminarImagen(DeleteView):
    model = Imagenes 
    template_name = 'Base/Imagen/eliminar_imagen.html' 

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            imagen = self.get_object()
            imagen.estado = False
            imagen.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Base:listar_imagen')
class MostrarImagen(View):
    model = Imagenes
    template_name = 'Base/Imagen/imagen.html'
    form_class = ImagenForm

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name, self.get_context_data())

    def get_context_data(self,**kwargs):
         pk = self.kwargs.get('pk')
         context = {}
         context['imagen'] = Imagenes.objects.filter(pk=pk,estado=True)

         return context
    
    
    
    

   
