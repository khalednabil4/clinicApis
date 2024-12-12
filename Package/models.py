from django.db import models

# Create your models here.
from User.models import SoftDeletionManager
from patient.models import *
from Service.models import *
class PackageType(models.Model):
    category=models.CharField(max_length=50)
    urgency_level = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    Organization = models.ForeignKey(Organization, related_name='PackageType', on_delete=models.PROTECT)

    objects = SoftDeletionManager()
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
    def __str__(self):
        return f"{self.category}"



class Package(models.Model):
    name = models.CharField(max_length=200)
    patient = models.ForeignKey(patient, related_name='Package', on_delete=models.CASCADE)
    PackageType = models.ForeignKey(PackageType, related_name='Package', on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    StartDate = models.DateField()
    EndDate = models.DateField(null=True,blank=True)
    attributes=models.JSONField(null=True,blank=True)
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeletionManager()
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
    def __str__(self):
        return f"{self.name}"

class PackageService(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='PackageService')
    Service = models.ForeignKey(Service, on_delete=models.CASCADE,related_name='PackageService')
    special_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeletionManager()
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
    class Meta:
        unique_together = ['package', 'Service']
    def __str__(self):
        return f"{self.service} in {self.package.name}"