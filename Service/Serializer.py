from rest_framework import serializers

from User.Serializer import *

from  .models import *
from  Clinic.Serializer import *
class ServiceSerializer(serializers.ModelSerializer):

    doctor = AdministratorProfileSerializer(read_only=True)
    class Meta:
        model = Service
        fields = "__all__"
class ServiceCreateSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(
        queryset=Administrator.objects.all(),
        required=True
    )
    class Meta:
        model = Service
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        # Get the request context to access the logged-in user

        request = kwargs.get('context', {}).get('request', None)
        if   request.user.is_superuser:
            self.fields['doctor'].queryset = Administrator.objects.all()
        else:
            client = Administrator.objects.get(id=request.user.id)
            self.fields['doctor'].queryset = Administrator.objects.filter(Organization=client.Organization,IsDoctor=True)

        super().__init__(*args, **kwargs)

