from django.db import models

class Appointment(models.Model):
    name=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)    
    gender=models.CharField(max_length=50) 
    appointment_date=models.CharField(max_length=50)
    appointment_session=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    message=models.CharField(max_length=200)
    class Meta:
        db_table:"appointment"

class Covid19(models.Model):
    pName=models.CharField(max_length=50)
    age=models.CharField(max_length=3)    
    sex=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    date_of_checkup=models.CharField(max_length=50)
    pMobile=models.CharField(max_length=50)
    weight =models.CharField(max_length=50)
    pulse =models.CharField(max_length=50)
    blood_pressure=models.CharField(max_length=50)
    temprature =models.CharField(max_length=50)
    spo2=models.CharField(max_length=50)
    comorbidity_existing_disease=models.CharField(max_length=50)
    symptoms=models.CharField(max_length=50)
    class Meta:
        db_table:"covid19"
        