from django.db import models

# Create your models here.

from appCombustibles.models import Combustible
from appUsuarios.models import User

class Cisterna(models.Model):
    tipo_combustible = models.ForeignKey(Combustible, on_delete=models.CASCADE)
    cantidad_litros = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.tipo_combustible} - {self.cantidad_litros}"
