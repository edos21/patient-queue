from django.db import models
from django.utils import timezone

class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class Station(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order'] 

class PatientStatus(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    entry_date = models.DateTimeField(default=timezone.now)
    exit_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.patient.full_name} at {self.station.name}"
