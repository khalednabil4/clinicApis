from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User, Group
import datetime
import random
import string
from django.contrib.auth.hashers import make_password
from django.utils.text import slugify
from django.contrib.auth.models import UserManager
class AdministratorManager(models.Manager):
    def get_by_organization(self, organization):
        return self.filter(Organization=organization, is_deleted=False)
class SoftDeletionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                message="Phone number must be entered in the format: '+999999999'."
                                        " Up to 15 digits "
                                        "allowed.")

class CustomUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=11, null=True, blank=True, unique=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['id']
        verbose_name_plural = "01_CustomUser"

def generate_unique_code():
    # Generate a random string of length 8 (you can adjust the length and characters)
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))



class Organization(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True,null=True)
    org_id = models.CharField(max_length=100, unique=True,blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeletionManager()

    def delete(self):
        self.is_deleted = True
        self.save()

    def save(self, *args, **kwargs):
        if self.is_deleted:
            self.name = f"{self.name}-{slugify(self.id)}"
            self.org_id = f"{self.org_id}-{slugify(self.id)}"
        super(Organization, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name_plural = "03_Organization"

    def __str__(self):
        return str(self.name)

class Specialist(models.Model):
    name=models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    Organization = models.ForeignKey(Organization, related_name='Specialists', null=True, on_delete=models.PROTECT)
    code = models.CharField(max_length=100, unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.is_deleted:
            self.username = f"{self.name}-{slugify(self.id)}"
        if not self.code:
            self.code = generate_unique_code()  # Generate unique code
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.name)


class Administrator(CustomUser):
    name=models.CharField(max_length=100, blank=True, default="User")
    profile_img = models.ImageField(upload_to='Admins', default='/Admins/doctor.jpg')
    bio = models.CharField(max_length=100, blank=True, default="User Here")
    SpecialInformation=models.TextField(null=True,blank=True)
    IsDoctor=models.BooleanField(default=0)
    is_deleted = models.BooleanField(default=False)
    Specialist = models.ManyToManyField(Specialist, related_name='administrators', blank=True)
    Organization = models.ForeignKey(Organization, related_name='administrators', null=True, on_delete=models.PROTECT)
    objects = SoftDeletionManager()
    administrator_objects =AdministratorManager()
    class Meta:
        verbose_name = "02_Administrator"
        verbose_name_plural = "02_Administrators"
        ordering = ['id']
    def clean(self):
        if self.email:
            self.email = UserManager.normalize_email(self.email)

    def __str__(self) -> str:
        return self.username

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()



    def save(self, *args, **kwargs):
        if self.id is None:
            self.password = make_password(self.password)
        if self.is_deleted:
            self.username = f"{self.username}-{slugify(self.id)}"
        if self.phone_number == "":
            self.phone_number = None
        super(Administrator, self).save(*args, **kwargs)

# class patient(User):
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=100, unique=True, blank=True, null=True)
#     profile_img = models.ImageField(blank=True,null=True,upload_to='patient', default='/patient/account.png')
#     Organization = models.ForeignKey(Organization, related_name='Clinic', null=True, on_delete=models.CASCADE)
#     birth_date = models.DateField(null=True)
#     @property
#     def age(self):
#         if self.birth_date:
#             age = datetime.date.today() - self.birth_date
#             return int(age.days / 365.25)
#         return None  # In case birth_date is not set
#     class Meta:
#         verbose_name = "patient"
#         verbose_name_plural = "patient"
#         permissions = ()
#     def __str__(self):
#         return self.name
#     def save(self, *args, **kwargs):
#         if not self.code:
#             self.code = generate_unique_code()  # Generate unique code
#         super().save(*args, **kwargs)
