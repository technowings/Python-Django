from django.urls import path,include
from loginweb import views

urlpatterns=[
    path('login',views.web_login,name='login'),
    path('register',views.web_register,name='register'),
    path('dashboard',views.web_dashboard,name='dashboard'),
    path('logout',views.web_logout,name='logout'),
    path('appointment',views.admin_appointment,name='admin_appointment'),
    path('covid',views.admin_covid19,name='admin_covid19'),
    path('registration',views.admin_Pregister,name='admin_pregister'),
    path('export_appoint',views.export_appointments_xls,name='export_appointment'),
    path('history',views.admin_history,name='history'),
    path('prescription',views.admin_prescr,name='prescr'),
    path('addprescription',views.admin_addPrec,name='addprescr'),
    path('changepassword',views.change_pass,name='changepassword'),
]