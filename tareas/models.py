
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creacion = models.DateTimeField(auto_now_add=True)   #automatico
    fecha_cierre = models.DateTimeField(null=True)          #permite vacio
    importancia = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo