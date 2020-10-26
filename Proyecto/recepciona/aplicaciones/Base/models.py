from django.db import models
#from aplicaciones.usuario.models import *


class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        abstract = True

#Aqui estaran todos los modulos relacionados con las direcciones
class Regiones(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_nombre = models.CharField('Nombre region', max_length = 100)
    region_ordinal = models.CharField('Region ordinal', max_length = 4)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'
    def __str__(self):
        return self.region_nombre

class Provincias(models.Model):
    provincia_id = models.AutoField(primary_key=True)
    provincia_nombre = models.CharField('Nombre provincia', max_length = 100)
    region = models.ForeignKey(Regiones, on_delete = models.CASCADE)


    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
    def __str__(self):
        return self.provincia_nombre

class Comunas(models.Model):
    comuna_id = models.AutoField(primary_key=True)
    comuna_nombre = models.CharField('Nombre comuna', max_length = 100)
    provincia = models.ForeignKey(Provincias, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
    def __str__(self):
        return self.comuna_nombre

class CentroDeportivo(ModeloBase):
     usuario_id = models.ForeignKey('usuario.Usuario', on_delete = models.CASCADE )
     nombre = models.CharField('Nombre', max_length = 40)
     direccion = models.CharField('Direccion', max_length = 100)
     region = models.ForeignKey(Regiones, on_delete = models.CASCADE)     
     provincia = models.ForeignKey(Provincias, on_delete = models.CASCADE)
     comuna = models.ForeignKey(Comunas, on_delete = models.CASCADE)

     class Meta:
        verbose_name = 'Centro deportivo'
        verbose_name_plural = 'Centros deportivos'

     def __str__(self):
        return self.nombre      

#A partir de aqui se definen los modelos para canchas
class Superficie(ModeloBase):
    nombre = models.CharField('Nombre', max_length=40, unique = True)

    class Meta:
        verbose_name = 'Superficie'
        verbose_name_plural = 'Superficies'

    def __str__(self):
        return self.nombre

class Tipo_cancha(ModeloBase):    
    nombre = models.CharField('Nombre', max_length=40)

    class Meta:
        verbose_name = 'Tipo de cancha'
        verbose_name_plural = 'Tipos de canchas'

    def __str__(self):
        return self.nombre


class Servicio(ModeloBase):    
    nombre = models.CharField('Nombre', max_length=40) 
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    def __str__(self):
        return self.nombre




class Cancha(ModeloBase):
    usuario_id = models.ForeignKey('usuario.Usuario', on_delete = models.CASCADE)
    nombre = models.CharField('Nombre', max_length=40)
    descripcion = models.CharField('Descripcion', max_length=40)
    valor = models.CharField('Valor hora', max_length=40)
    servicios = models.ManyToManyField(Servicio)
    imagen = models.ImageField('Imagen principal', upload_to = 'cancha_img/', max_length = 255, null = True)
    tipo_cancha = models.ForeignKey(Tipo_cancha, on_delete = models.CASCADE)
    superficie = models.ForeignKey(Superficie, on_delete = models.CASCADE)
    centro_dep = models.ForeignKey(CentroDeportivo, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Cancha'
        verbose_name_plural = 'Canchas'
    def __str__(self):
        return self.nombre

    


class Imagenes(ModeloBase):
    cancha_id = models.ForeignKey(Cancha, on_delete = models.CASCADE, related_name = 'imagen_cancha')
    imagen_cancha = models.ImageField('Imagen de cancha', upload_to = 'cancha/', max_length = 255, null = True)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
 


class Color(ModeloBase):
    codigo = models.CharField('Codigo del color', max_length = 50)
    color_name = models.CharField('Nombre de color', max_length = 50)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'
    def __str__(self):
        return self.color_name
class Dias(ModeloBase):
    day_number = models.IntegerField()
    day_name = models.CharField('Nombre del dia', max_length = 50)
    
    class Meta:
        verbose_name = 'Dia'
        verbose_name_plural = 'Dias'
    def __str__(self):
        return self.day_name
class Horario(ModeloBase):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    title = models.CharField('title', max_length = 50)
    hora_inicio = models.CharField('hora inicio', max_length=8, null=True)
    hora_termino = models.CharField('hora termino', max_length=8, null=True)
    dia = models.ForeignKey(Dias, on_delete = models.CASCADE)
    color = models.ForeignKey(Color, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
    

#Aqui iran los datos relacionados con las reservas

class Reserva(ModeloBase):
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    date_start = models.CharField('date_start',max_length=19)
    date_end = models.CharField('date_end', max_length=19)
    color = models.ForeignKey(Color, on_delete = models.CASCADE)


    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'









