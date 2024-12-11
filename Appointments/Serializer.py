from rest_framework import serializers

from User.Serializer import *

from  .models import *

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