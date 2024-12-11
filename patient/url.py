from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [

    #
    path('patientOp/add/', patientOp.as_view()),
    path('patientOp/edit/<int:pk>/', patientOp.as_view()),
    path('patientOp/delete/<int:pk>/', patientOp.as_view()),
    path('GetpatientById/<int:pk>/', patientOp.as_view()),
    path('getpatientListFiltered/', getpatientListFiltered.as_view()),


]