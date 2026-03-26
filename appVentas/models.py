from django.db import models

# Create your models here.
from appClientes.models import Cliente
from appUsuarios.models import Usuario
from appCombustibles.models import Combustible

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    combustible = models.ForeignKey(Combustible, on_delete=models.CASCADE)
    litros = models.DecimalField(max_digits=10, decimal_places=2)
    monto_bs = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    empleado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta {self.id}"
