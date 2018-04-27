from django.db import models

# Create your models here.

class Museo(models.Model):
    nombre = models.CharField(max_length=32)
    direccion = models.CharField(max_length=32)
    def __str__(self):
        return self.nombre
