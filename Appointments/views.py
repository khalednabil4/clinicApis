from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from User.ExpectionDecorator import handle_api_exception

from User.Serializer import MyTokenObtainPairSerializer
from rest_framework.response import Response
from .models import *
from  .Serializer import *

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
        kwargs['context'] = {'request': self.request}
        return self.serializer_class(*args, **kwargs)

    def get_serializer_viw(self, *args, **kwargs):
        kwargs['context'] = {'request': self.request}
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

# Create your views here.
class daysOp(GenralCRUD):
    permission_classes = [IsAuthenticated]
    model = Days
    serializer_class = DaysCreateSerializer
    serializer_class_view=DaysSerializer



class getDaysListFiltered(APIView):
        permission_classes = [IsAuthenticated]

        @handle_api_exception(error_message="Not Found", code=400)
        def get(self, request):
            if  request.user.is_superuser:
                data = Days.objects.all()
            else:

                client = Administrator.objects.get(id=request.user.id)
                data = Days.objects.filter(Admin__Organization=client.Organization)
            serializer = DaysSerializer(data, many=True)
            response_data = {
                'count': data.count(),
                'data': serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)





class DoctoravailabilityOp(GenralCRUD):
    permission_classes = [IsAuthenticated]
    model = Doctoravailability
    serializer_class = DoctoravailabilityCreateSerializer
    serializer_class_view=DoctoravailabilitySerializer




class getDoctoravailabilityListFiltered(APIView):
        permission_classes = [IsAuthenticated]

        @handle_api_exception(error_message="Not Found", code=400)
        def get(self, request):
            if  request.user.is_superuser:
                data = Doctoravailability.objects.all()
            else:

                client = Administrator.objects.get(id=request.user.id)
                data = Doctoravailability.objects.filter(Doctor__Organization=client.Organization)
            serializer = DoctoravailabilitySerializer(data, many=True)
            response_data = {
                'count': data.count(),
                'data': serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)