from rest_framework import serializers

from User.Serializer import *

from  .models import *
from  Clinic.Serializer import *
class DaysSerializer(serializers.ModelSerializer):

    Admin = AdministratorProfileSerializer(read_only=True)
    class Meta:
        model = Days
        fields = [
            'id', 'name', 'HourTo',
            'HourFrom', 'date', 'Admin'
        ]
class DaysCreateSerializer(serializers.ModelSerializer):
    Admin = serializers.PrimaryKeyRelatedField(
        queryset=Administrator.objects.all(),
        required=True
    )
    class Meta:
        model = Days
        fields = [
            'id', 'name', 'HourTo',
            'HourFrom', 'date', 'Admin'
        ]

    def __init__(self, *args, **kwargs):
        # Get the request context to access the logged-in user

        request = kwargs.get('context', {}).get('request', None)
        if request.user.is_superuser:
            self.fields['Admin'].queryset = Administrator.objects.all()
        else:
            client = Administrator.objects.get(id=request.user.id)
            self.fields['Admin'].queryset = Administrator.objects.filter(Organization=client.Organization)

        super().__init__(*args, **kwargs)






class DoctoravailabilitySerializer(serializers.ModelSerializer):

    Doctor = AdministratorProfileSerializer(read_only=True)
    Day=DaysSerializer
    class Meta:
        model = Doctoravailability
        fields = [
            'id', 'DateFrom', 'Day',
            'DateTo', 'LevelImportant', 'TimeAdd', 'Status','Doctor'
        ]
class DoctoravailabilityCreateSerializer(serializers.ModelSerializer):
    Doctor = serializers.PrimaryKeyRelatedField(
        queryset=Administrator.objects.all(),
        required=True
    )
    class Meta:
        model = Doctoravailability
        fields = [
            'id', 'DateFrom', 'Day',
            'DateTo', 'LevelImportant', 'TimeAdd', 'Status','Doctor'
        ]

    def __init__(self, *args, **kwargs):
        # Get the request context to access the logged-in user

        request = kwargs.get('context', {}).get('request', None)
        if request.user.is_superuser:
            self.fields['Doctor'].queryset = Administrator.objects.all()
        else:
            client = Administrator.objects.get(id=request.user.id)
            self.fields['Doctor'].queryset = Administrator.objects.filter(Organization=client.Organization)

        super().__init__(*args, **kwargs)


class ScheduleSerializer(serializers.ModelSerializer):

    Doctoravailability = DoctoravailabilitySerializer(read_only=True)
    clinic=ClinicSerializer(read_only=True)
    class Meta:
        model = Schedule
        fields = "__all__"
class ScheduleCreateSerializer(serializers.ModelSerializer):
    Doctoravailability = serializers.PrimaryKeyRelatedField(
        queryset=Doctoravailability.objects.all(),
        required=True
    )
    clinic=serializers.PrimaryKeyRelatedField(
        queryset=Clinic.objects.all(),
        required=True
    )
    class Meta:
        model = Schedule
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if  request.user.is_superuser:
            self.fields['Doctoravailability'].queryset = Doctoravailability.objects.all()
            self.fields['clinic'].queryset = Clinic.objects.all()
        else:
            client = Administrator.objects.get(id=request.user.id)
            self.fields['Doctoravailability'].queryset = Doctoravailability.objects.filter(Doctor__Organization=client.Organization)
            #Edit display Clinic same Specelist
            self.fields['clinic'].queryset = Clinic.objects.all()

        super().__init__(*args, **kwargs)