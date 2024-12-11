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