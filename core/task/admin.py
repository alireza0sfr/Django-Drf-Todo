from django.contrib import admin

from .models import Task, Category


class CustomTaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('id', 'author', 'title', 'content', 'status', 'category', 'priority', 'created_date')
    list_filter = list_display
    search_fields = list_display
    ordering = list_display


class CustomCategoryAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('id', 'name', 'created_date')
    list_filter = list_display
    search_fields = list_display
    ordering = list_display


admin.site.register(Task, CustomTaskAdmin)
admin.site.register(Category, CustomCategoryAdmin)
