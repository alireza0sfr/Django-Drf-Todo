from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser', 'is_verified')
    list_filter = list_display
    search_fields = ('email',)
    ordering = search_fields


admin.site.register(User, CustomUserAdmin)
