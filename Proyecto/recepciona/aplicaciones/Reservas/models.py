from django.db import models
from usuarios.models import Usuario
from Cancha.models import cancha

class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract=True

class reserva(ModeloBase):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Cancha_r = models.ForeignKey(cancha, on_delete=models.CASCADE)
    hora_inicio = models.TimeField('Desde')
    hora_fin= models.TimeField('Hasta')
    fecha_reserva = models.DateField('Fecha de reserva')
    

    
