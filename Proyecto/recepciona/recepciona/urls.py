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
from django.views.static import serve

from django.urls import path, include, re_path
from aplicaciones.Base.views import Inicio, home, MisReservas, Descripcion_cancha
from django.contrib.auth.decorators import login_required
from aplicaciones.usuario.views import Login, logoutUsuario
from aplicaciones.Base import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/',include(('aplicaciones.usuario.urls','usuarios'))),
    path('Base/',include(('aplicaciones.Base.urls','Base'))),
    path('Base/',login_required(Inicio.as_view()), name = 'index'),
    path('',login_required(home), name = 'home'),    
    path('accounts/login/',Login.as_view(), name = 'Login'),
    path('logout/' ,login_required(logoutUsuario), name = 'logout'),
    path('mis_reservas/<int:pk>',MisReservas.as_view(), name = 'mis_reservas'),
    path('Descripcion_cancha/<int:pk>',Descripcion_cancha.as_view(), name = 'Descripcion_cancha'),
  
]
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]