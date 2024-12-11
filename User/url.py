from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('Test/', Test.as_view(), name='token_obtain_pair'),
    #Login
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #OrganizationOp
    path('OrganizationOp/add/', OrganizationOp.as_view()),
    path('OrganizationOp/edit/<int:pk>/', OrganizationOp.as_view()),
    path('OrganizationOp/delete/<int:pk>/', OrganizationOp.as_view()),
    path('GetOrganizationById/<int:pk>/', OrganizationOp.as_view()),
    path('getOrganizationListFiltered/', getOrganizationListFiltered.as_view()),
    #Admin
    path('AdministratorOp/add/', AdministratorOp.as_view()),
    path('AdministratorOp/edit/<int:pk>/', AdministratorOp.as_view()),
    path('AdministratorOp/delete/<int:pk>/', AdministratorOp.as_view()),
    path('AdministratorById/<int:pk>/', AdministratorOp.as_view()),
   path('getAdministratorListFiltered/', getAdministratorListFiltered.as_view()),
#Specialist
    path('SpecialistOp/add/', SpecialistOp.as_view()),
    path('SpecialistOp/edit/<int:pk>/', SpecialistOp.as_view()),
    path('SpecialistOp/delete/<int:pk>/', SpecialistOp.as_view()),
    path('SpecialistById/<int:pk>/', SpecialistOp.as_view()),
    path('getSpecialistListFiltered/', getSpecialistListFiltered.as_view()),

]