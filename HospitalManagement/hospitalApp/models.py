from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse






# class Patient(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     date_of_birth = models.DateField()
#     address = models.CharField(max_length=255)
    
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'

# class Doctor(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     # specialties = models.ManyToManyField('Specialty')
#     schedule = models.TextField()
    
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'


class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    date = models.DateField()
    time = models.TimeField()
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return f'{self.patient} with {self.doctor} on {self.date} at {self.time}'

# class Prescription(models.Model):
#     medication = models.CharField(max_length=255)
#     dosage = models.CharField(max_length=255)
#     instructions = models.TextField()
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     def __str__(self):
#         return f'{self.medication} prescribed to {self.patient} by {self.doctor}'



# this one is for contact us like
class contactEnquiry(models.Model):
    your_name =models.CharField(max_length=50)
    your_email =models.CharField(max_length=100)
    subject =models.CharField(max_length=50)
    messages =models.CharField(max_length=500)



