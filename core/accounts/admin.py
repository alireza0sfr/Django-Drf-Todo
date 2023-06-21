from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User
from accounts.models import UserBan, IPBan


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'id', 'is_staff', 'is_active', 'is_superuser', 'is_anonymous', 'is_verified')
    list_filter = list_display
    search_fields = ('email', 'id')
    ordering = search_fields
    fieldsets = (
        ('Authentication', {'fields': ('email', 'password')}),
        ('Permission', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_anonymous', 'is_verified')}),
        ('Group Permissions', {'fields': ('groups', 'user_permissions')}),
        ('Metadata', {'fields': ('last_login',)}),

    )
    add_fieldsets = (
        ('Authentication', {'fields': ('email', 'password1', 'password2')}),
        ('Permission', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_anonymous', 'is_verified')})
    )

    def save_form(self, request, form, change):
        if not change:

            if form.cleaned_data['is_superuser']:
                form.instance = self.model.objects.create_superuser(form.cleaned_data['email'],
                                                                    form.cleaned_data['password1'])

            else:
                form.instance = self.model.objects.create_user(form.cleaned_data['email'],
                                                               form.cleaned_data['password1'])
        return super().save_form(request, form, change)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserBan)
admin.site.register(IPBan)
