from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(Administrator)
admin.site.register(Organization)
admin.site.register(Specialist)
#
# admin.site.register(Organization)