from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminDjango
from django.contrib.auth.models import Group
from apps.user.models import User


class UserAdmin(UserAdminDjango):
    fieldsets = UserAdminDjango.fieldsets + (
        (None, {'fields': ('alias', 'avatar')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'alias', 'avatar', 'password1', 'password2')
        }),
    )

    def is_registered(self, obj):
        return obj.groups.filter(name='registered').exists()
    is_registered.short_description = 'Es Usuario Registrado'
    is_registered.boolean = True

    def is_collaborator(self, obj):
        return obj.groups.filter(name='collaborator').exists()
    is_collaborator.short_description = 'Es Colaborador'
    is_collaborator.boolean = True

    def is_moderator(self, obj):
        return obj.groups.filter(name='moderator').exists()
    is_moderator.short_description = 'Es Moderador'
    is_moderator.boolean = True

    def add_to_registered(self, request, queryset):
        registered_group = Group.objects.get(name='registered')
        for user in queryset:
            user.groups.add(registered_group)
        self.message_user(
            request, "Los usuarios seleccionados fueron añadidos al grupo 'registered'.")
    add_to_registered.short_description = 'Agregar a Usuarios Registrados'

    actions = [add_to_registered]

    list_display = ['username', 'email', 'is_staff', 'is_superuser',
                    'is_registered', 'is_collaborator', 'is_moderator']

    ordering = ['-date_joined']

    search_fields = ['username', 'email', 'alias', 'id']


admin.site.register(User, UserAdmin)


