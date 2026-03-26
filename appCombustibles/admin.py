from django.contrib import admin
from appCombustibles.models import Combustible
# Register your models here.


@admin.register(Combustible)
class CombustibleAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'precio_por_litro', 'stock', 'actualizado_en')
    search_fields = ('tipo',)
