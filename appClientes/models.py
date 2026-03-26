from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    ci = models.CharField(max_length=20, unique=True)
    litros_gasolina_mes = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
