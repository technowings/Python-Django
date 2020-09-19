from django.shortcuts import render,redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from django.conf import settings as conf_set

# Create your views here.


def web_index(request):
    context = {"home_page": "active"} # its for nav menu active
    return render(request,'websiteviews/index.html',context)


def web_profile(request):
    context = {"profile_page": "active"} # its for nav menu active
    return render(request,'websiteviews/profile.html',context)

def web_services(request):
    context = {"services_page": "active"} # its for nav menu active
    return render(request,'websiteviews/services.html',context)

def web_appointment(request):
    context = {"appointment_page": "active"} # its for nav menu active
    return render(request,'websiteviews/appointment.html',context) 

def web_contact(request):
    context = {"contact_page": "active"} # its for nav menu active
    return render(request,'websiteviews/contact.html',context)    

def getFormData(request):
     person_name=request.POST.get('name', '')
     subject = request.POST.get('subject', '')
     message = request.POST.get('message','')
     from_email = request.POST.get('email', '')
     print_msg="Name : "+person_name+"Subject : "+subject+"Message : "+message+"User Mail :"+from_email
     if subject and message and from_email and person_name:
        try:
            print(print_msg)          
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Your message has Print. Thank you!')
     else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
  