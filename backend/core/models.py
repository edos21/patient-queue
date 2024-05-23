from django.db import models
from django.utils import timezone

class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

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

    def __str__(self):
        return self.name
    
    @property
    def current_patient(self):
        current_patient_status = self.patients.filter(exit_date__isnull=True).order_by('-entry_date').first()
        if current_patient_status:
            return current_patient_status.patient.full_name
        return None

    class Meta:
        ordering = ['order'] 

class PatientStatus(models.Model):
    patient = models.ForeignKey(Patient, related_name='stations', on_delete=models.CASCADE)
    station = models.ForeignKey(Station, related_name='patients', on_delete=models.CASCADE)
    entry_date = models.DateTimeField(default=timezone.now)
    exit_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.patient.full_name} at {self.station.name}"
