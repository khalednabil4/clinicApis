from django.db import models
from django.db.models import Q, CheckConstraint
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from User.ExpectionDecorator import handle_api_exception
from User.models import *
DAY_CHOICES = [
    ("MONDAY", 'Monday'),
    ("TUESDAY", 'Tuesday'),
    ("WEDNESDAY", 'Wednesday'),
    ("THURSDAY", 'Thursday'),
    ("FRIDAY", 'Friday'),
    ("SATURDAY", 'Saturday'),
    ("SUNDAY", 'Sunday'),
]
DoctoravailabilitySatus = [
    ("Process", 'Process'),
    ("Cancel", 'Cancel'),
    ("Rejected", 'Rejected by the administration'),
    ("waiting", 'waiting'),
    ("approval", 'approval'),
    ("AnotherDate", 'AnotherDate'),
]
ImportantLevel = [
    ("important", '1'),
    ("Mid", '2'),
    ("normal", '3')

]
class Days(models.Model):
    name = models.CharField(max_length=20, choices=DAY_CHOICES)
    Admin=models.ForeignKey(Administrator, related_name='DaysOpen',on_delete=models.PROTECT)
    HourTo=models.TimeField()
    HourFrom=models.TimeField()
    is_deleted = models.BooleanField(default=False)
    date = models.DateField()
    objects = SoftDeletionManager()
    def save(self, *args, **kwargs):
        if self.is_deleted:
            self.username = f"{self.name}-{self.date}-{slugify(self.id)}"

    def delete(self):
        self.is_deleted = True
        self.save()
    def __str__(self):
        return f"{self.name} - {self.date}"


class Doctoravailability(models.Model):
    DateFrom=models.TimeField()
    Day= models.ForeignKey(Days, on_delete=models.PROTECT, related_name='Doctoravailability')
    DateTo=models.TimeField()
    LevelImportant = models.CharField(max_length=20, choices=ImportantLevel,blank=True)
    TimeAdd=models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    Status = models.CharField(max_length=50, choices=DoctoravailabilitySatus,default=1)
    Doctor=models.ForeignKey(Administrator, related_name='admin', on_delete=models.PROTECT)
    objects = SoftDeletionManager()
    def delete(self):
        self.is_deleted = True
        self.save()
    def save(self, *args, **kwargs):
        if self.is_deleted:
            self.username = f"{self.TimeAdd}-{slugify(self.id)}"

@receiver(pre_save, sender=Doctoravailability)
def validate_doctor_is_doctor(sender, instance, **kwargs):
        if not instance.Doctor.IsDoctor:
           raise ValidationError("The assigned user must be a doctor.")