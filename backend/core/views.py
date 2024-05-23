from rest_framework import viewsets

from .serializer import PatientSerializer, StationSerializer, PatientStatusSerializer
from .models import Patient, Station, PatientStatus

class PatientsView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class StationsView(viewsets.ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects.all()

class PatientStatusView(viewsets.ModelViewSet):
    serializer_class = PatientStatusSerializer
    queryset = PatientStatus.objects.all()