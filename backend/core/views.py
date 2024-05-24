from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
#from django.core.mail import send_mail
#from django.conf import settings

from .serializer import PatientSerializer, StationSerializer, PatientStatusSerializer
from .models import Patient, Station, PatientStatus

class PatientsView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.filter(is_active=True).order_by('created_at')

class StationsView(viewsets.ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects.all()

class PatientStatusView(viewsets.ModelViewSet):
    serializer_class = PatientStatusSerializer
    queryset = PatientStatus.objects.all()

class NextPatientView(APIView):
    def post(self, request, station_id):
        try:
            station = Station.objects.get(id=station_id)
        except Station.DoesNotExist:
            return Response({"message": "Station not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if PatientStatus.is_any_patient_active_in_station(station):
            return Response({"message": "There is already a patient in this station."}, status=status.HTTP_400_BAD_REQUEST)

        next_patient = Patient.objects.filter(
            is_active=True
        ).exclude(
            id__in=PatientStatus.objects.filter(station=station).values_list('patient_id', flat=True)
        ).order_by('created_at').first()
        
        if not next_patient:
            return Response({"message": "No patient in the waiting list."}, status=status.HTTP_404_NOT_FOUND)
        
        if PatientStatus.is_patient_active_in_any_station(next_patient):
            return Response({"message": "Patient is already assigned to a station."}, status=status.HTTP_400_BAD_REQUEST)
        
        PatientStatus.objects.create(patient=next_patient, station=station)

        '''
        TODO: implement send different types of message, maybe similar to dependency injection
        send_mail(
            'Your turn at the station',
            f'Dear {next_patient.full_name}, it\'s your turn at the {station.name} station.',
            settings.DEFAULT_FROM_EMAIL,
            [next_patient.email],  
        )'''
        
        return Response({"message": f"Patient {next_patient.full_name} has been moved to station {station.name}."}, status=status.HTTP_200_OK)
    
class EndTurnView(APIView):
    def post(self, request, station_id):
        try:
            station = Station.objects.get(id=station_id)
        except Station.DoesNotExist:
            return Response({"error": "Station not found"}, status=status.HTTP_404_NOT_FOUND)
        
        current_status = PatientStatus.objects.filter(station=station, exit_date__isnull=True).first()

        if not current_status:
            return Response({"message": "No current patient in this station"}, status=status.HTTP_404_NOT_FOUND)
        
        current_status.exit_date = timezone.now()
        current_status.save()

        if station.is_last_station():
            patient = current_status.patient
            patient.is_active = False
            patient.save()
            return Response({"message": f"Patient {patient.full_name} has completed all stations and is now inactive"}, status=status.HTTP_200_OK)
        
        return Response({"message": "Patient has exited the current station"}, status=status.HTTP_200_OK)