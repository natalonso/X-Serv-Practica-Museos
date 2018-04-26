from django.db import models

# Create your models here.

class Museo(models.Model):
    nombre = models.CharField(max_length=32)
    direccion = models.CharField(max_length=32)
    distrito = models.CharField(max_length=32)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.nombre
