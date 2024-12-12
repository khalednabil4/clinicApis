from rest_framework import serializers

from User.Serializer import *

from  .models import *
from  Clinic.Serializer import *
from patient.Serializer import *
from patient.models import *
from patient.models import *
from Service.Serializer import *
from Appointments.Serializer import *
class ReservationSerializer(serializers.ModelSerializer):

    patient = PatientProfileSerializer(read_only=True)
    service=ServiceSerializer(read_only=True)
    Schedule = ScheduleSerializer(read_only=True)
    class Meta:
        model = Reservation
        fields = "__all__"
class ReservationCreateSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(
        queryset=patient.objects.all(),
        required=True
    )
    service = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(),
        required=True
    )
    Schedule = serializers.PrimaryKeyRelatedField(
        queryset=Schedule.objects.all(),
        required=True
    )
    class Meta:
        model = Reservation
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        # Get the request context to access the logged-in user

        request = kwargs.get('context', {}).get('request', None)
        if   request.user.is_superuser:
            self.fields['patient'].queryset = patient.objects.all()
            self.fields['service'].queryset = Service.objects.all()
            self.fields['Schedule'].queryset = Schedule.objects.all()

        else:
            client = Administrator.objects.get(id=request.user.id)
            self.fields['patient'].queryset = patient.objects.filter(Organization=client.Organization)
            self.fields['Schedule'].queryset = Schedule.objects.filter(clinic__Specialist__Organization=client.Organization)

        super().__init__(*args, **kwargs)

