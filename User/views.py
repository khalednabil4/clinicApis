from django.http import Http404
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from .ExpectionDecorator import handle_api_exception
from .querys import *
from User.Serializer import MyTokenObtainPairSerializer
from rest_framework.response import Response
from .models import *
from  .Serializer import *
#Login
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class Test(APIView):
    permission_classes = []
    def  get(self,request):
        client = Administrator.objects.get(id=request.user.id)
        data = Organization.objects.filter(name=client.Organization)
        organization = request.user.Organization
        administrators = Administrator.administrator_objects.get_by_organization(organization)

        print(data)
        return Response(data, status=status.HTTP_200_OK)


class GenralCRUD(APIView):
    model = None
    serializer_class = None
    serializer_class_view = None
    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404
    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get_serializer_viw(self, *args, **kwargs):
        return self.serializer_class_view(*args, **kwargs)
    @handle_api_exception(error_message="Add False", code=500)
    def post(self, request, format=None):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"data": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

    @handle_api_exception(error_message="Get Error", code=500)
    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = self.get_serializer_viw(instance)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    @handle_api_exception(error_message="Update False", code=500)
    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"data": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

    @handle_api_exception(error_message="delete False",code=500)
    def delete(self, request, pk, format=None):
            instance = self.get_object(pk)
            instance.delete()
            return Response({"data": "Delete successful"}, status=status.HTTP_200_OK)

#Specialist
class SpecialistOp(GenralCRUD):
    permission_classes = [IsAuthenticated]
    model = Specialist
    serializer_class = SpecialistSerializer
    serializer_class_view=SpecialistSerializer

class getSpecialistListFiltered(APIView):
        permission_classes = [IsAuthenticated]

        @handle_api_exception(error_message="Not Found", code=400)
        def get(self, request):
            if request.user.is_superuser:
                data = Specialist.objects.all()
            else:
                client = Administrator.objects.get(id=request.user.id)
                data = Specialist.objects.filter(Organization=client.Organization)
            serializer = SpecialistSerializer(data, many=True)
            response_data = {
                'count': data.count(),
                'data': serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)
#Admin
class AdministratorOp(GenralCRUD):
    permission_classes = [IsAuthenticated]
    model = Administrator
    serializer_class = AdministratorCreateSerializer
    serializer_class_view=AdministratorProfileSerializer

class getAdministratorListFiltered(APIView):
        permission_classes = [IsAuthenticated]

        @handle_api_exception(error_message="Not Found", code=400)
        def get(self, request):
            if request.user.is_superuser:
                data = Administrator.objects.all()
            else:
                client = Administrator.objects.get(id=request.user.id)
                data = Administrator.objects.filter(Organization=client.Organization)
            serializer = AdministratorProfileSerializer(data, many=True)
            response_data = {
                'count': data.count(),
                'data': serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)
    #Org
class OrganizationOp(GenralCRUD):
    permission_classes = [IsAuthenticated]
    model = Organization
    serializer_class = OrganizationSerializer
    serializer_class_view=OrganizationSerializer
class getOrganizationListFiltered(APIView):
    permission_classes = [IsAuthenticated]
    @handle_api_exception(error_message="Not Found", code=400)
    def  get(self,request):
            if request.user.is_superuser:
                data = Organization.objects.all()
            else:
                    client = Administrator.objects.get(id=request.user.id)
                    data = Organization.objects.filter(id=client.Organization)
            serializer = OrganizationSerializer(data, many=True)
            response_data = {
                'count': data.count(),
                'data': serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)

