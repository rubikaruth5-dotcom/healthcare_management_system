from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'phone',
        'specialization',
        'department',
        'experience',
        'is_available'
    )

    search_fields = ('name', 'email', 'specialization')

    list_filter = ('department', 'is_available')