from django.contrib import admin
from appCisternas.models import Cisterna
# Register your models here.


@admin.register(Cisterna)
class CisternaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_combustible', 'cantidad_litros', 'usuario', 'fecha_ingreso')
    list_filter = ('tipo_combustible', 'fecha_ingreso')