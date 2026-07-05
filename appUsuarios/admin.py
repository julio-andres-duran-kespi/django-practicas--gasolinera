from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from appUsuarios.models import User

User = get_user_model()

admin.site.register(User)


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'is_active', 'created_at')
    search_fields = ('email', 'full_name')

