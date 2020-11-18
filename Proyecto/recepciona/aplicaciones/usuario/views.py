from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from aplicaciones.direccion.models import Regiones, Provincias, Comunas
from .models import Usuario, Centro
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, TemplateView
from .forms import FormularioLogin, FormularioUsuario, CentroForm, EditarPerfilForms

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispath(self, request, *args, **kwargs):
        if request.user.is_authenticated:            
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispath(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class ListadoUsuario(ListView):
    model = Usuario
    
    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():
           
            return HttpResponse(serialize('json',self.get_queryset()),'application/json')
        else:
            return redirect('usuarios:inicio_usuarios')





class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                    nuevo_usuario = Usuario(
                        email=form.cleaned_data.get('email'),
                        username=form.cleaned_data.get('username'),
                        nombres=form.cleaned_data.get('nombres'),
                        apellidos=form.cleaned_data.get('apellidos'),
                        role=form.cleaned_data.get('role')
                    )
                    nuevo_usuario.set_password(form.cleaned_data.get('password1'))
                    nuevo_usuario.save()
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
            return redirect('usuarios:inicio_usuarios')
class EditarUsuario(UpdateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/editar_usuario.html'
    
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
            return redirect('usuarios:inicio_usuarios')
class EliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar_usuario.html'
    

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            usuario = self.get_object()
            usuario.usuario_activo = False
            usuario.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('usuarios:inicio_usuarios')

class MiPerfil(TemplateView):
    template_name = 'usuarios/mi_perfil.html'

    def get_context_data(self,**kwargs):
         
         
         context = {}
         context['user'] = Usuario.objects.all()
         
        
         return context

class EditarPerfil(UpdateView):
    model = Usuario
    form_class = EditarPerfilForms
    template_name = 'usuarios/editar_perfil.html'
    
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST, files = request.FILES,instance = self.get_object())
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
            return redirect('usuarios:inicio_usuarios')
    




class ListadoCentro(View):
    model = Centro
    form_class = CentroForm
    template_name = 'usuarios/mi_centro/listar_centro.html'
    
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
    model = Centro
    template_name = 'usuarios/mi_centro/centro.html'
    form_class = CentroForm
    success_url = reverse_lazy('usuarios:listar_centro')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')

        context = super(ActualizarCentro, self).get_context_data(**kwargs)
        context["region"] = Regiones.objects.all()  
        context["provincia"] = Provincias.objects.all()
        context["comuna"] = Comunas.objects.all()
        context["obj"] = Centro.objects.filter(pk=pk).first()
        return context

class CrearCentro(CreateView):
    model = Centro
    template_name = 'usuarios/mi_centro/crear_centro.html'
    form_class = CentroForm
    success_url = reverse_lazy('Base:listar_centro')
    def get_context_data(self, **kwargs):
        context = super(CrearCentro, self).get_context_data(**kwargs)
        context["region"] = Regiones.objects.all()  
        context["provincia"] = Provincias.objects.all()
        context["comuna"] = Comunas.objects.all()
        return context
class EliminarCentro(DeleteView):
    model = Centro  

    def post(self, request, pk, *args, **kwargs):
        object = Centro.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('usuario:listar_centro')
    
