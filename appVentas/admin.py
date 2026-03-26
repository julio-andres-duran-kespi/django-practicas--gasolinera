from django.contrib import admin
from appVentas.models import Venta
# Register your models here.



@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'combustible', 'litros', 'monto_bs', 'empleado', 'fecha_hora')
    list_filter = ('combustible', 'fecha_hora')
    search_fields = ('cliente__nombre',)
