from django.db import models
from usuarios.models import Usuario

class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True



class Superficie(ModeloBase):
    nombre = models.CharField('Nombre',max_length=40, unique = True)

    class Meta:
        verbose_name = 'Superficie'
        verbose_name_plural = 'Superficies'

    def __str__(self):
        return self.nombre

class Tipo_cancha(ModeloBase):    
    nombre = models.CharField('Nombre',max_length=40)

    class Meta:
        verbose_name='Tipo de cancha'
        verbose_name_plural='Tipos de canchas'

    def __str__(self):
        return self.nombre


class Servicio(ModeloBase):
    nombre = models.CharField('Nombre', max_length=40) 
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    def __str__(self):
        return self.nombre

class cancha(ModeloBase):
    nombre = models.CharField('Nombre', max_length=40)
    descripcion = models.CharField('Descripcion', max_length=40)
    direccion = models.CharField('Direccion', max_length=40)
    valor = models.CharField('Valor hora', max_length=40)
    servicios =  models.ManyToManyField(Servicio)
    tipo_cancha = models.ForeignKey(Tipo_cancha, on_delete = models.CASCADE)
    superfice =  models.ForeignKey(Superficie, on_delete = models.CASCADE)
    usuario_cancha = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cancha'
        verbose_name_plural = 'Canchas'
    def __str__(self):
        return self.nombre
class Dias(ModeloBase):
    nombre = models.CharField('Dia', max_length=20)

    class Meta:
        verbose_name='Dia'
        verbose_name_plural='Dias'

    def __str__(self):
        return self.nombre

class Horario(ModeloBase):
    cancha = models.ForeignKey(cancha, on_delete=models.CASCADE)
    hora_inicio = models.TimeField('hora inicio')
    hora_termino = models.TimeField('hora termino')
    dia = models.ForeignKey(Dias, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Horario'
        verbose_name_plural='Horarios'
