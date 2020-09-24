from django.contrib import admin
from django.urls import path,include
from website import views
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('',views.web_index,name='index'),
    path('appointment',views.web_appointment,name='appointment'),
    path('consultation',views.web_consultation,name='consultation'),
    path('diagnostic',views.web_diagnostic,name='diagnostic'),
    path('pharmacy',views.web_pharmacy,name='pharmacy'),
    path('contactus',views.web_contact,name='contact'),
                     
]
