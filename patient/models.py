from django.db import models
from User.models import *
# Create your models here.

class patient(CustomUser):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True, blank=True, null=True)
    profile_img = models.ImageField(blank=True,null=True,upload_to='patient', default='/patient/account.png')
    Organization = models.ForeignKey(Organization, related_name='patient', null=True, on_delete=models.PROTECT)
    birth_date = models.DateField(null=True)
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeletionManager()
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
    def clean(self):
        if self.email:
            self.email = UserManager.normalize_email(self.email)
    @property
    def age(self):
        if self.birth_date:
            age = datetime.date.today() - self.birth_date
            return int(age.days / 365.25)
        return None  # In case birth_date is not set
    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patient"
        ordering = ['id']
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.is_deleted:
            self.username = f"{self.username}-{slugify(self.id)}"
        if not self.code:
            self.code = generate_unique_code()  # Generate unique code
        super().save(*args, **kwargs)



class PatientHistory(models.Model):
    DateTO=models.DateField()
    DateFrom=models.DateField()
    Doctor=models.CharField(max_length=50,blank=True,null=True)
    Doc = models.ImageField(blank=True, null=True, upload_to='PatientDoc')
    patient= models.ForeignKey(patient, on_delete=models.CASCADE, related_name='PatientHistory')
    PatientVitals=models.JSONField(null=True,blank=True)
    Note=models.TextField(blank=True,null=True)
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeletionManager()
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()