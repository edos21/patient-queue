from django.db import models
from django.utils import timezone

class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    @property
    def current_station(self):
        latest_station = self.stations.filter(exit_date__isnull=True).order_by('-entry_date').first()
        if latest_station:
            return latest_station.station.name
        return "On Wait"

class Station(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    @property
    def current_patient(self):
        current_patient_status = self.patients.filter(exit_date__isnull=True).first()
        return current_patient_status.patient.full_name if current_patient_status else None
    
    def is_last_station(self):
        return not Station.objects.filter(order__gt=self.order).exists()

    class Meta:
        ordering = ['order'] 

class PatientStatus(models.Model):
    patient = models.ForeignKey(Patient, related_name='stations', on_delete=models.CASCADE)
    station = models.ForeignKey(Station, related_name='patients', on_delete=models.CASCADE)
    entry_date = models.DateTimeField(default=timezone.now)
    exit_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.full_name} at {self.station.name}"

    @classmethod
    def is_patient_active_in_any_station(cls, patient):
        return cls.objects.filter(patient=patient, exit_date__isnull=True).exists()

    @classmethod
    def is_any_patient_active_in_station(cls, station):
        return cls.objects.filter(station=station, exit_date__isnull=True).exists()