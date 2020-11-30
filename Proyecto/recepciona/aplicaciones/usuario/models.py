from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico!')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,email,password):
        user = self.create_user(
            email,
            username = username,        
            password = password
        )
        user.usuario_administrador = True
        user.save()
        return user


class Centro(models.Model):
    nombre = models.CharField('Nombre de centro deportivo', max_length=200, blank = True, null = True)
    descripcion = models.CharField('Descripcion del centro', max_length = 500, null = True)
    imagen_portada = models.ImageField('Imagen de portada', upload_to='perfil/', max_length=200,blank = True,null = True)
    acerca = models.CharField('Acerca de nosotros', max_length = 1000, null = True)
    logo = models.ImageField('Logo', upload_to='logo/', max_length=200,blank = True,null = True)
    direccion = models.CharField('Direccion', max_length = 100)    
    region = models.ForeignKey('direccion.Regiones', on_delete = models.CASCADE)
    provincia = models.ForeignKey('direccion.Provincias', on_delete = models.CASCADE)  
    comuna = models.ForeignKey('direccion.Comunas', on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre

class Role(models.Model):
    nombre = models.CharField('Nombre de role',max_length = 100, null = True)

    def __str__(self):
        return self.nombre

class Usuario(AbstractBaseUser):
    
    username = models.CharField('Nombre de usuario',unique = True, max_length=100)
    nombres = models.CharField('Nombres', max_length=200, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length=200,blank = True, null = True)
    direccion = models.CharField('Direccion', max_length = 100, null= True)
    region = models.ForeignKey('direccion.Regiones', on_delete = models.CASCADE, null = True)  
    provincia = models.ForeignKey('direccion.Provincias', on_delete = models.CASCADE, null= True)
    comuna = models.ForeignKey('direccion.Comunas', on_delete = models.CASCADE, null= True)
    email = models.EmailField('Correo Electrónico', max_length=254,unique = True)   
    centro = models.ForeignKey(Centro, on_delete = models.CASCADE, null = True)
    role = models.ForeignKey(Role, on_delete = models.CASCADE, null = True)
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/', max_length=200,null = True)
    usuario_activo = models.BooleanField(default = True)
    usuario_administrador = models.BooleanField(default = False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        permissions = [('permiso_desde_codigo','Este es un permiso creado desde código'),
                        ('segundo_permiso_codigo','Segundo permiso creado desde codigo')]

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'
    
        
    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador


    




