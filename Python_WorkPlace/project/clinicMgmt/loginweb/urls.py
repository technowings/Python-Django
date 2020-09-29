from django.urls import path,include
from . import views

urlpatterns=[
    path('login',views.web_login,name='login'),
    path('register',views.web_register,name='register'),
    path('dashboard',views.web_dashboard,name='dashboard'),
]