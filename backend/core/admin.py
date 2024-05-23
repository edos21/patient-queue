from django.contrib import admin
from .models import Patient, Station, PatientStatus

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'phone_number', 'is_active')
    search_fields = ('full_name', 'phone_number')
    list_filter = ('is_active',)

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name',)
    ordering = ('order',)

@admin.register(PatientStatus)
class PatientStatusAdmin(admin.ModelAdmin):
    list_display = ('patient', 'station', 'entry_date', 'exit_date')
    search_fields = ('patient__full_name', 'station__name')
    list_filter = ('station', 'entry_date', 'exit_date')
    date_hierarchy = 'entry_date'
