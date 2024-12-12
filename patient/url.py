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

    path('PatientHistoryOp/add/', PatientHistoryOp.as_view()),
    path('PatientHistoryOp/edit/<int:pk>/', PatientHistoryOp.as_view()),
    path('PatientHistoryOp/delete/<int:pk>/', PatientHistoryOp.as_view()),
    path('GetPatientHistoryById/<int:pk>/', PatientHistoryOp.as_view()),
    path('getPatientHistoryListFiltered/', getPatientHistoryListFiltered.as_view()),
]