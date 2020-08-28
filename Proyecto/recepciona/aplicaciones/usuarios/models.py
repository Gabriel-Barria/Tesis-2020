from django.db import models


class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract=True

class Region(ModeloBase):
    nombre_region = models.CharField('Nombre region', max_length=40)

    class Meta:
        verbose_name='Region'
        verbose_name_plural='Regiones'
    def __str__(self):
        return self.nombre_region

class Comuna(ModeloBase):
    nombre_comuna = models.CharField('Nombre comuna', max_length=40)

    class Meta:
        verbose_name='Comuna'
        verbose_name_plural='Comunas'
    def __str__(self):
        return self.nombre_comuna

class Direccion(ModeloBase):
    comuna = models.ForeignKey(Comuna, on_delete = models.CASCADE)
    calle = models.CharField('Calle', max_length=100)
    numero = models.IntegerField('Numero')

    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'

class Roles(ModeloBase):
    nombre=models.CharField('Nombre',max_length=40)
    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.nombre


#crear modelo de usuario
class Usuario(ModeloBase):
    nombres=models.CharField('Nombres',max_length=40)
    direccion_usuario = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    contrasenia = models.CharField('Contraseña', max_length=40)
    apellidop= models.CharField('Apellido paterno', max_length=40)
    apellidom= models.CharField('Apellido materno', max_length=40)
    role = models.ForeignKey(Roles, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombres
