from django.urls import path
from .views import *

urlpatterns = [

    #
    path('PackageTypeOp/add/', PackageTypeOp.as_view()),
    path('PackageTypeOp/edit/<int:pk>/', PackageTypeOp.as_view()),
    path('PackageTypeOp/delete/<int:pk>/',PackageTypeOp.as_view()),
    path('GetPackageTypeById/<int:pk>/', PackageTypeOp.as_view()),
    path('getPackageTypeListFiltered/', getPackageTypeListFiltered.as_view()),

    path('PackageOp/add/', PackageOp.as_view()),
    path('PackageOp/edit/<int:pk>/', PackageOp.as_view()),
    path('PackageOp/delete/<int:pk>/', PackageOp.as_view()),
    path('GetPackageById/<int:pk>/', PackageOp.as_view()),
    path('getPackageListFiltered/', getPackageListFiltered.as_view()),

    path('PackageServiceOp/add/', PackageServiceOp.as_view()),
    path('PackageServiceOp/edit/<int:pk>/', PackageServiceOp.as_view()),
    path('PackageServiceOp/delete/<int:pk>/', PackageServiceOp.as_view()),
    path('GetPackageServiceById/<int:pk>/', PackageServiceOp.as_view()),
    path('getPackageServiceListFiltered/', getPackageServiceListFiltered.as_view()),

]