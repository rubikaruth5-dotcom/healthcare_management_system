from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'is_active', 'created_at')
    search_fields = ('name', 'location')
    list_filter = ('is_active',)