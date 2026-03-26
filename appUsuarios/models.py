from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=255)

    ROLES = [
        ('Administrador', 'Administrador'),
        ('Empleado', 'Empleado'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
