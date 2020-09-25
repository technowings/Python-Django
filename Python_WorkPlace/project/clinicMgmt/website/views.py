from django.shortcuts import render,redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm,AppointmentForm
from django.conf import settings as conf_set
from website.models import Appointment


# Create your views here.


def web_index(request):
    cname=conf_set.CNAME
    if request.method == 'GET':
        appointment_form = AppointmentForm()
    else:
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            person_name=appointment_form.cleaned_data['pName']
            age = appointment_form.cleaned_data['age']
            sex = appointment_form.cleaned_data['sex']
            aDate = appointment_form.cleaned_data['appointment_date']
            pMobile = appointment_form.cleaned_data['pMobile']
            #message = appointment_form.cleaned_data['p_message']
            message_send="\n Patient Name : "+person_name
            saveAppoint=Appointment()
            try:
                saveAppoint.name=person_name
                saveAppoint.page=age
                saveAppoint.gender=sex
                saveAppoint.ap_date=aDate
                saveAppoint.mobile=pMobile
                saveAppoint.save()
                

                print(message_send)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    context = {
        'appointment_form': appointment_form,
        'home_page': 'active',
        "company":cname
    }        
    return render(request,'websiteviews/index.html',context)

def web_consultation(request):
    cname=conf_set.CNAME
    context = {"consultation_page": "active","company":cname} # its for nav menu active
    return render(request,'websiteviews/consultation.html',context)

def web_diagnostic(request):
    cname=conf_set.CNAME
    context = {"diagnostic_page": "active","company":cname} # its for nav menu active
    return render(request,'websiteviews/diagnostic.html',context)    

def web_pharmacy(request):
    cname=conf_set.CNAME
    context = {"pharmacy_page": "active","company":cname} # its for nav menu active
    return render(request,'websiteviews/pharmacy.html',context)  



def web_contact(request):
    cname=conf_set.CNAME
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
            from_email=conf_set.EMAIL_HOST_USER
            try:
                send_mail(subject,message_send,from_email, ['bodhi.technology@outlook.com'])
                print(from_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    context = {
        'form': form,
        'contact_page': 'active',
        "company":cname
    }        
    return render(request, "websiteviews/contact.html",context)





  