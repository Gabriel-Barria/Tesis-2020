"""recepciona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from django.urls import path, include, re_path
from aplicaciones.Base.views import Inicio, Home, MisReservas, Descripcion_cancha, Filtro_cancha,MostrarCalendario, Inicio_home
from django.contrib.auth.decorators import login_required
from aplicaciones.usuario.views import Login, logoutUsuario, RegistroUsuario
from aplicaciones.Base import views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/',include(('aplicaciones.usuario.urls','usuarios'))),
    path('Base/',include(('aplicaciones.Base.urls','Base'))),
    path('Base/',login_required(Inicio.as_view()), name = 'index'),
    path('',Home.as_view(), name = 'home'),  
    path('inicio_home/',Inicio_home.as_view(),name='inicio_home'), 
    path('filtro-cancha/<int:pk>/',login_required(Filtro_cancha.as_view()), name = 'filtro-cancha'),
    path('mostrar-calendario/<int:pk>/',login_required(MostrarCalendario.as_view()), name = 'mostrar-calendario'), 
    path('accounts/login/',Login.as_view(), name = 'Login'),
    path('logout/' ,login_required(logoutUsuario), name = 'logout'),
    path('mis_reservas/<int:pk>',MisReservas.as_view(), name = 'mis_reservas'),
    path('registrar_usuario/',RegistroUsuario.as_view(),name='registro_usuario'),
    path('Descripcion_cancha/<int:pk>',Descripcion_cancha.as_view(), name = 'Descripcion_cancha'),
    
  
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]