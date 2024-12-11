from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from .models import *
from .models import Administrator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        print(self.user)
        superstatus=False
        user_type=None
        flag=True
        if hasattr(self.user, 'administrator'):
            Administrator = self.user.administrator
            user_type = "administrator"
            UserGroup = Administrator.groups
            superstatus=Administrator.is_superuser
        elif hasattr(self.user, 'patient'):
            patient = self.user.patient
            user_type = "patient"
            UserGroup = patient.groups
            superstatus = patient.is_superuser
        else:
            raise AuthenticationFailed("Unauthorized access")
        if superstatus ==True:
           group_permissions=Permission.objects.all()
        else:
         group_permissions = UserGroup.permissions.all()
        list=[]
        for group in group_permissions:
            list.append(group.codename)
        list.append(user_type)
        data['username'] = self.user.username
        data['Permission'] = list
        return data
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id','org_id','name','address']
class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['id','name']
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class AdministratorProfileSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    Organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = Administrator
        fields = [
            'id', 'username', 'phone_number', 'Organization',
            'groups', 'is_active', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

class AdministratorCreateSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        many=True,
        required=False
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Administrator
        fields = ['id', 'username', 'phone_number', 'password', 'Organization', 'groups', 'is_active']

        def create(self, validated_data):
            # Extract groups if provided
            groups = validated_data.pop('groups', [])
            password = validated_data.pop('password')
            validated_data['password'] = make_password(password)
            Administrator = super().create(validated_data)
            if groups:
                Administrator.groups.set(groups)
            return Administrator