from django.db import models

# Create your models here.
class PatientRegister(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)    
    gender=models.CharField(max_length=50) 
    mobile=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    photo=models.ImageField(upload_to="register_patient/imgs",null=True)
    class Meta:
        db_table:"p_register"


class PatientPrec(models.Model):        
    prec=models.CharField(max_length=200)
    patient=models.ForeignKey(PatientRegister,on_delete=models.CASCADE,null=True)