from django.contrib import admin
from appClientes.models import Cliente

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ci', 'litros_gasolina_mes', 'creado_en')
    search_fields = ('nombre', 'ci')
