from django.contrib import admin
from appUsuarios.models import Usuario
# Register your models here.



@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'usuario', 'rol', 'creado_en')
    search_fields = ('nombre', 'usuario')
