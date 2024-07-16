"""
Django admin customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""
    ordering = ['id']
    list_display = ['email', 'name', 'is_staff']
    search_fields = ('email', 'name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_staff', 'is_superuser', 'is_active')}
        ),
        (_('Important Dates'), {'fields': ('last_login', )})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2',
                       'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    readonly_fields = ['last_login']


admin.site.register(models.CustomUser, UserAdmin)
admin.site.register(models.Recipe)
