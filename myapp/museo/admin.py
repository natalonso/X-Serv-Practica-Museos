from django.contrib import admin

# Register your models here.
from .models import Museo
#hacemos esto para trabajar en la interfaz del navegador
admin.site.register(Museo)
