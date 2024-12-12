from rest_framework import serializers
from User.Serializer import *
from  .models import *
class PatientProfileSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    Organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = patient
        fields = [
            'id', 'username', 'phone_number', 'Organization',
            'groups', 'is_active', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

class PatientCreateSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        many=True,
        required=False
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = patient
        fields = ['id', 'username', 'phone_number', 'password', 'Organization', 'groups', 'is_active']

        def create(self, validated_data):
            # Extract groups if provided
            groups = validated_data.pop('groups', [])
            password = validated_data.pop('password')
            validated_data['password'] = make_password(password)
            patient = super().create(validated_data)
            if groups:
                patient.groups.set(groups)
            return patient

class PatientHistorySerializer(serializers.ModelSerializer):
    patient = PatientProfileSerializer()
    class Meta:
        model = PatientHistory
        fields = "__all__"


class PatientHistoryCreateSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(
        queryset=patient.objects.all(),
        required=False
    )
    class Meta:
        model = PatientHistory
        fields = "__all__"

    def __init__(self, *args, **kwargs):


        request = kwargs.get('context', {}).get('request', None)
        if  request.user.is_superuser:
            self.fields['patient'].queryset = patient.objects.all()
        else:
            client = Administrator.objects.get(id=request.user.id)
            self.fields['patient'].queryset = patient.objects.filter(Organization=client.Organization)

        super().__init__(*args, **kwargs)
