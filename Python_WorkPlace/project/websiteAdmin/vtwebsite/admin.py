from django.contrib import admin
from .models import VTAbout,VTServices
from .models import VTPortfolioIot,VTPortfolioMob,VTPortfolioWeb
# Register your models here.

admin.site.register(VTAbout)
admin.site.register(VTServices)
admin.site.register(VTPortfolioWeb)
admin.site.register(VTPortfolioMob)
admin.site.register(VTPortfolioIot)