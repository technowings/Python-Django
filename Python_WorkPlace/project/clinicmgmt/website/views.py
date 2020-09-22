from django.shortcuts import render,redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from django.conf import settings as conf_set
from website.forms import ContactForm
from django.contrib import messages

# Create your views here.


def web_index(request):
    cname=conf_set.C_NAME
    #print(cname)
    context = {"home_page": "active",'cname':cname} # its for nav menu active
    return render(request,'websiteviews/index.html',context)


def web_profile(request):
    cname=conf_set.C_NAME
    context = {"profile_page": "active",'cname':cname} # its for nav menu active
    return render(request,'websiteviews/profile.html',context)

def web_services(request):
    cname=conf_set.C_NAME
    context = {"services_page": "active",'cname':cname} # its for nav menu active
    return render(request,'websiteviews/services.html',context)

def web_appointment(request):
    context = {"appointment_page": "active"} # its for nav menu active
    return render(request,'websiteviews/appointment.html',context) 

# def web_contact(request):
#     context = {"contact_page": "active"} # its for nav menu active
#     return render(request,'websiteviews/contact.html',context)   

def web_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            person_name=form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            user_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message_send="\n Name : "+person_name+"\n Message : "+message+"\n User Email : "+user_email
            #messages.info(request,message_send) 
            #from_email=conf_set.EMAIL_HOST_USER
            try:
                #send_mail(subject,message_send,from_email, ['bodhi.technology@outlook.com'])
                print(message_send)
                #messages.info(request,'Hello send') 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            #messages.info(request,'Hello')    
            #return redirect('contact')
    context = {
        'form': form,
        'contact_page': 'active',
    }        
    return render(request, "websiteviews/contact.html",context)     

# def getFormData(request):
#      if request.method=='POST':
#         person_name=request.POST['name']
#         subject = request.POST['subject']
#         message = request.POST['message']
#         from_email = request.POST['email']
#         print_msg="Name : "+person_name+"Subject : "+subject+"Message : "+message+"User Mail :"+from_email
#         print(print_msg)
        
#      else:
#           return render(request,'websiteviews/contact.html') 
    
#      return render(request,'websiteviews/contact.html') 
    #  if subject and message and from_email and person_name:
    #     try:
    #         print(print_msg)          
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     return render('websiteviews/index.html') #HttpResponse('Your message has Print. Thank you!')
    #  else:
    #     # In reality we'd use a form class
    #     # to get proper validation errors.
    #     return HttpResponse('Make sure all fields are entered and valid.')
  