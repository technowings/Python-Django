from django.contrib import admin
from django.urls import path,include
from . import views
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('',views.web_index,name='index'),
    path('services',views.web_services,name='services'),
    path('profile',views.web_profile,name='profile'),
    path('appointment',views.web_appointment,name='appointment'),
    path('contactus',views.web_contact,name='contact'),
    # path('getformdata',views.getFormData,name='getformdata'),
                     
]
