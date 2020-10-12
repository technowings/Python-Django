from django.db import models

# Create your models here.

class VTServices(models.Model):
    imge=models.ImageField(upload_to='webimg/servicesImg')
    name=models.CharField(max_length=200)
    desc=models.TextField()

class VTAbout(models.Model):
    imge=models.ImageField(upload_to='webimg/aboutImg')
    name=models.CharField(max_length=200)
    desc=models.TextField()

class VTPortfolioMob(models.Model):
    hname=models.CharField(max_length=200)
    pname=models.CharField(max_length=200)
    imge=models.ImageField(upload_to='webimg/portFolioMobImg')

class VTPortfolioWeb(models.Model):
    hname=models.CharField(max_length=200)
    pname=models.CharField(max_length=200)
    imge=models.ImageField(upload_to='webimg/portFolioWebImg')    

class VTPortfolioIot(models.Model):
    hname=models.CharField(max_length=200)
    pname=models.CharField(max_length=200)
    imge=models.ImageField(upload_to='webimg/portFolioIotImg')

    
    



# Create your models here.
