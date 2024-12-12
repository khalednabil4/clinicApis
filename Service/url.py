from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [

    #
    path('ServiceOp/add/', ServiceOp.as_view()),
    path('ServiceOp/edit/<int:pk>/', ServiceOp.as_view()),
    path('ServiceOp/delete/<int:pk>/', ServiceOp.as_view()),
    path('GetServiceById/<int:pk>/', ServiceOp.as_view()),
    path('getServiceListFiltered/', getServiceListFiltered.as_view()),

]