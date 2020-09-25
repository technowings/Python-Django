from django.db import models

class Appointment(models.Model):
     name=models.CharField(max_length=100)
     page=models.CharField(max_length=50)    
     gender=models.CharField(max_length=50)
     ap_date=models.CharField(max_length=50)
     mobile=models.CharField(max_length=50) 

