from django.db import models

# Create your models here.

class Combustible(models.Model):
    tipo = models.CharField(max_length=50, unique=True)
    precio_por_litro = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo
