from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'patient',
        'doctor',
        'appointment_date',
        'appointment_time',
        'status'
    )

    search_fields = (
        'patient__name',
        'doctor__name'
    )

    list_filter = (
        'status',
        'appointment_date'
    )

    ordering = ('-appointment_date',)