from rest_framework import serializers
from .models import *

from User.Serializer import *




class ClinicSerializer(serializers.ModelSerializer):
    Specialist=SpecialistSerializer(read_only=True)
    class Meta:
        model = Clinic
        fields = "__all__"
class ClinicCreateSerializer(serializers.ModelSerializer):
    Specialist = serializers.PrimaryKeyRelatedField(
        queryset=Specialist.objects.all(),
        required=True
    )
    class Meta:
        model = Clinic
        fields =  "__all__"

    def __init__(self, *args, **kwargs):


        request = kwargs.get('context', {}).get('request', None)
        if request.user.is_superuser:
            self.fields['Specialist'].queryset = Administrator.objects.all()
        else:
            client = Administrator.objects.get(id=request.user.id)
            self.fields['Specialist'].queryset = Administrator.objects.filter(Specialist__Organization=client.Organization)

        super().__init__(*args, **kwargs)