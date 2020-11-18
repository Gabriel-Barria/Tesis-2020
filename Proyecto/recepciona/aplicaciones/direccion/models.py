from django.db import models

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

