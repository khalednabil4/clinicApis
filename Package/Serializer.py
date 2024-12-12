

from rest_framework import serializers

from  .models import *
from  Clinic.Serializer import *
from User.Serializer import *
from patient.models import *
from patient.Serializer import *
from User.models import *
from Service.Serializer import *
class PackageTypeSerializer(serializers.ModelSerializer):
    Organization = OrganizationSerializer(read_only=True)
    class Meta:
        model = PackageType
        fields = "__all__"

class PackageTypeCreateSerializer(serializers.ModelSerializer):
    Organization = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all(),
        required=True
    )

    class Meta:
        model =PackageType
        fields = "__all__"


class PackageSerializer(serializers.ModelSerializer):
    patient = PatientProfileSerializer (read_only=True)
    PackageType=PackageTypeSerializer(read_only=True)
    class Meta:
        model = Package
        fields = "__all__"

class PackageCreateSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(
        queryset=patient.objects.all(),

        required=True
    )
    PackageType=serializers.PrimaryKeyRelatedField(
        queryset=PackageType.objects.all(),
        required=True
    )
    class Meta:
        model = Package
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if  request.user.is_superuser:
            self.fields['patient'].queryset = patient.objects.all()
            self.fields['PackageType'].queryset = PackageType.objects.all()
        else:
            client = Administrator.objects.get(id=request.user.id)
            self.fields['patient'].queryset = patient.objects.filter(Organization=client.Organization)
            self.fields['PackageType'].queryset = PackageType.objects.filter(PackageType__Organization=client.Organization)

        super().__init__(*args, **kwargs)





class PackageServiceSerializer(serializers.ModelSerializer):
    package = PackageSerializer (read_only=True)
    Service=ServiceSerializer(read_only=True)
    class Meta:
        model = PackageService
        fields = "__all__"

class PackageServiceCreateSerializer(serializers.ModelSerializer):
    package = serializers.PrimaryKeyRelatedField(
        queryset=Package.objects.all(),
        required=True
    )
    Service=serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(),
        required=True
    )
    class Meta:
        model = PackageService
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if    request.user.is_superuser:
            self.fields['package'].queryset = Package.objects.all()
            self.fields['Service'].queryset = Service.objects.all()
        else:
            client = Administrator.objects.get(id=request.user.id)
            self.fields['package'].queryset = Package.objects.filter(PackageType__Organization=client.Organization)
            self.fields['Service'].queryset = Service.objects.filter(doctor__Organization=client.Organization)

        super().__init__(*args, **kwargs)




