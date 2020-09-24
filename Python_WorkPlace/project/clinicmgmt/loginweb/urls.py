from django.urls import path,include
from . import views

urlpatterns=[
    path('login',views.web_login,name='login'),
    path('dashboard',views.web_dashboard,name='dashboard'),
]