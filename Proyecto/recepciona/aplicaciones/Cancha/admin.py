from django.contrib import admin
from .models import Superficie, Tipo_cancha, Servicio, cancha, Horario, Dias

admin.site.register(Superficie)
admin.site.register(Tipo_cancha)
admin.site.register(Servicio)
admin.site.register(cancha)
admin.site.register(Dias)
admin.site.register(Horario)


# Register your models here.
