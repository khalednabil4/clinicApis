from django.db import models

# Create your models here.
from User.models import generate_unique_code
from User.models import *
from django.utils.text import slugify
class Clinic(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    code = models.CharField(max_length=100, unique=True, blank=True, null=True)
    IsAvailable=models.BooleanField(default=1)
    AvaiableTimeFrom=models.DateField(blank=True,null=True)
    AvaiableTimeTo=models.DateField(blank=True,null=True)
    is_deleted = models.BooleanField(default=False)
    Specialist = models.ForeignKey(Specialist, related_name='Clinic', on_delete=models.CASCADE, null=True)
    objects = SoftDeletionManager()
    def __str__(self):
        return str(self.name)
    def save(self, *args, **kwargs):
        if self.is_deleted:
            self.username = f"{self.name}-{slugify(self.id)}"
        if not self.code:
            self.code = generate_unique_code()  # Generate unique code
        super().save(*args, **kwargs)