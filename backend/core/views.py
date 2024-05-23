from rest_framework import viewsets

from .serializer import PatientSerializer
from .models import Patient

class PatientsView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()