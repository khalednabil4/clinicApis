from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [


    path('daysOp/add/', daysOp.as_view()),
    path('daysOp/edit/<int:pk>/', daysOp.as_view()),
    path('daysOp/delete/<int:pk>/', daysOp.as_view()),
    path('daystById/<int:pk>/', daysOp.as_view()),
    path('getdaysListFiltered/', getDaysListFiltered.as_view()),

    path('DoctoravailabilityOp/add/', DoctoravailabilityOp.as_view()),
    path('DoctoravailabilityOp/edit/<int:pk>/', DoctoravailabilityOp.as_view()),
    path('DoctoravailabilityOp/delete/<int:pk>/', DoctoravailabilityOp.as_view()),
    path('DoctoravailabilityById/<int:pk>/', DoctoravailabilityOp.as_view()),
    path('getDoctoravailabilityListFiltered/', getDoctoravailabilityListFiltered.as_view()),

    path('ScheduleOp/add/', ScheduleOp.as_view()),
    path('ScheduleOp/edit/<int:pk>/', ScheduleOp.as_view()),
    path('ScheduleOp/delete/<int:pk>/', ScheduleOp.as_view()),
    path('ScheduleById/<int:pk>/', ScheduleOp.as_view()),
    path('getScheduleListFiltered/', getScheduleListFiltered.as_view()),

]