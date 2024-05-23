from rest_framework import serializers
from .models import Patient, Station, PatientStatus

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'full_name', 'birth_date', 'phone_number', 'is_active']

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name', 'order']

class PatientStatusSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    station = StationSerializer(read_only=True)

    class Meta:
        model = PatientStatus
        fields = ['id', 'patient', 'station', 'entry_date', 'exit_date']