from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from appUsuarios.models import User



@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ('email',)
    search_fields = ('email', 'full_name')
    list_display = ('email', 'full_name', 'is_active', 'is_staff', 'created_at', 'last_login')
    readonly_fields = ('created_at', 'last_login')
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'created_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'is_active', 'created_at')
    search_fields = ('email', 'full_name')

