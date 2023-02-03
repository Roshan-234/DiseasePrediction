from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# this one is for contact us like
class contactEnquiry(models.Model):
    your_name =models.CharField(max_length=50)
    your_email =models.EmailField(unique=True)
    subject =models.CharField(max_length=50)
    messages =models.CharField(max_length=500)



# this one is for appointment us like
class Appointment(models.Model):
    name =models.CharField(max_length=50)
    email =models.EmailField(unique=False)
    date =models.DateField(blank=True)
    time =models.TimeField(blank=True)
    messages =models.CharField(max_length=500, null=True)



