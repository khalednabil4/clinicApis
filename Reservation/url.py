from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [


    path('ReservationOp/add/', ReservationOp.as_view()),
    path('ReservationOp/edit/<int:pk>/', ReservationOp.as_view()),
    path('ReservationOp/delete/<int:pk>/', ReservationOp.as_view()),
    path('GetReservationById/<int:pk>/', ReservationOp.as_view()),
    path('getReservationListFiltered/', getReservationListFiltered.as_view()),

]