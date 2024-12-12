from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [

    path('ClinicOp/add/', ClinicOp.as_view()),
    path('ClinicOp/edit/<int:pk>/', ClinicOp.as_view()),
    path('ClinicOp/delete/<int:pk>/', ClinicOp.as_view()),
    path('ClinicById/<int:pk>/', ClinicOp.as_view()),
    path('getClinicListFiltered/', getClinicListFiltered.as_view()),

]