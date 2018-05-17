from django.db import models

# Create your models here.

class Museo(models.Model):
    entidad = models.CharField(max_length=32)
    nombre = models.CharField(max_length=32)
    descripcion = models.CharField(max_length=32)
    horario = models.CharField(max_length=32)
    transporte = models.CharField(max_length=32)
    accesibilidad = models.CharField(max_length=32)
    url = models.CharField(max_length=32)
    via = models.CharField(max_length=32)
    clase = models.CharField(max_length=32)
    tipo = models.CharField(max_length=32)
    num = models.CharField(max_length=32)
    localidad = models.CharField(max_length=32)
    provincia = models.CharField(max_length=32)
    codigo = models.CharField(max_length=32)
    barrio = models.CharField(max_length=32)
    distrito = models.CharField(max_length=32)
    coordenadax = models.CharField(max_length=32)
    coordenaday = models.CharField(max_length=32)
    latitud = models.CharField(max_length=32)
    longitud = models.CharField(max_length=32)
    telefono = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    comentarios = models.IntegerField()

    def __str__(self):
        return self.nombre

class Museo_Usuario(models.Model):
    usuario = models.CharField(max_length=532)
    id_museo = models.IntegerField()
    fecha = models.DateField()

class Comentario(models.Model):
    comentario = models.CharField(max_length=532)
    id_museo = models.CharField(max_length=532)

class Usuario(models.Model):
    color = models.CharField(max_length=532)
    tamaño = models.CharField(max_length=532)
