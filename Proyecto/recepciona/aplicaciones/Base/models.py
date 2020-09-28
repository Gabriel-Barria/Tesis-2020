from django.db import models

class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True

#Aqui estaran todos los modulos relacionados con las direcciones
class Region(ModeloBase):
    nombre_region = models.CharField('Nombre region', max_length=40)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'
    def __str__(self):
        return self.nombre_region

class Comuna(ModeloBase):
    nombre_comuna = models.CharField('Nombre comuna', max_length=40)
    region = models.ForeignKey(Region, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
    def __str__(self):
        return self.nombre_comuna

class Ciudad(ModeloBase):
    nombre_ciudad = models.CharField('Ciudad', max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
    def __str__(self):
        return self.nombre_ciudad

#A partir de aqui se ingresan los modelos para usuarios

class Roles(ModeloBase):
    nombre = models.CharField('Nombre', max_length=40)
    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.nombre


#crear modelo de usuario

class Persona(ModeloBase):
    nombres = models.CharField('Nombres', max_length=40)
    apellidop = models.CharField('Apellido paterno', max_length=40)
    apellidom = models.CharField('Apellido materno', max_length=40)
    direccion = models.CharField('Direccion', max_length=60)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    email = models.EmailField('e-mail')


class Usuario(ModeloBase):     
    contrasenia = models.CharField('Contraseña', max_length=40)
    role = models.ForeignKey(Roles, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Ubicacion(ModeloBase):
    lat = models.CharField('Latitud', max_length=100)
    lng = models.CharField('Longitud', max_length=100)


class CentroDeportivo(ModeloBase):
     Nombre = models.CharField('Nombre', max_length = 40)
     direccion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)  

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
    estado = models.BooleanField('Estado', default=True)
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
    servicios = models.ManyToManyField(Servicio)
    tipo_cancha = models.ForeignKey(Tipo_cancha, on_delete = models.CASCADE)
    superfice = models.ForeignKey(Superficie, on_delete = models.CASCADE)
    centro_dep = models.ForeignKey(CentroDeportivo, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Cancha'
        verbose_name_plural = 'Canchas'
    def __str__(self):
        return self.nombre

class Horario(ModeloBase):
    cancha = models.ForeignKey(cancha, on_delete=models.CASCADE)
    hora_inicio = models.TimeField('hora inicio')
    hora_termino = models.TimeField('hora termino')
    dia = models.CharField('Dia de semana', max_length=15)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

#Aqui iran los datos relacionados con las reservas

class reserva(ModeloBase):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Cancha_r = models.ForeignKey(cancha, on_delete=models.CASCADE)
    hora_inicio = models.TimeField('Desde')
    hora_fin = models.TimeField('Hasta')
    fecha_reserva = models.DateField('Fecha de reserva')

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'









