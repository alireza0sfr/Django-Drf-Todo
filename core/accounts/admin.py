from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, Profile
from accounts.models import UserBan, IPBan


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'email', 'phone_number', 'is_staff', 'is_active', 'is_superuser', 'is_anonymous', 'is_verified')
    list_filter = list_display
    search_fields = ('id', 'email', 'phone_number')
    ordering = search_fields
    fieldsets = (
        ('Authentication', {'fields': ('email', 'password')}),
        ('Permission', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_anonymous', 'is_verified')}),
        ('Group Permissions', {'fields': ('groups', 'user_permissions')}),
        ('Metadata', {'fields': ('last_login', 'phone_number')}),

    )
    add_fieldsets = (
        ('Authentication', {'fields': ('email', 'password1', 'password2')}),
        ('Permission', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_anonymous', 'is_verified')}),
        ('Meta Data', {'fields': ('phone_number',)})
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



class CustomUserBanAdmin(admin.ModelAdmin):
    model = UserBan
    list_display = ('id', 'user', 'reason', 'description', 'until', 'created_date')
    list_filter = list_display
    search_fields = list_display
    ordering = list_display

    
class CustomIPBanAdmin(admin.ModelAdmin):
    model = IPBan
    list_display = ('id', 'ip', 'reason', 'description', 'until', 'created_date')
    list_filter = list_display
    search_fields = list_display
    ordering = list_display


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserBan, CustomUserBanAdmin)
admin.site.register(IPBan, CustomIPBanAdmin)
admin.site.register(Profile)
