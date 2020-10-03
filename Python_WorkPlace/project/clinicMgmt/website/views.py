from django.shortcuts import render,redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm,AppointmentForm,CovidForm
from django.conf import settings as conf_set
from website.models import Appointment,Covid19
from django.contrib import messages


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
            aSess= appointment_form.cleaned_data['appointment_session']
            pMobile = appointment_form.cleaned_data['pMobile']
            message = appointment_form.cleaned_data['p_message']
            saveAppoint=Appointment()
            try:
                saveAppoint.name=person_name
                saveAppoint.dob=age
                saveAppoint.gender=sex
                saveAppoint.appointment_date=aDate
                saveAppoint.appointment_session=aSess
                saveAppoint.mobile=pMobile
                saveAppoint.message=message
                saveAppoint.save()
                              
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

def web_covid19(request):
    cname=conf_set.CNAME
    if request.method == 'GET':
        form = CovidForm()
    else:
        form = CovidForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['pName']
            age=form.cleaned_data['age']
            sex=form.cleaned_data['sex']
            address=form.cleaned_data['address']
            date_of_checkup=form.cleaned_data['date_of_checkup']
            pMobile=form.cleaned_data['pMobile']
            weight=form.cleaned_data['weight']
            pulse=form.cleaned_data['pulse']
            blood_pressure=form.cleaned_data['blood_pressure']
            temprature=form.cleaned_data['temprature']
            spo2=form.cleaned_data['spo2']
            symptoms=form.cleaned_data['symptoms']
            comorbidity_existing_disease=form.cleaned_data['comorbidity_existing_disease']
            try:
                covid_obj=Covid19()
                covid_obj.pName=name
                covid_obj.age=age
                covid_obj.sex=sex
                covid_obj.address=address
                covid_obj.date_of_checkup=date_of_checkup
                covid_obj.pMobile=pMobile
                covid_obj.weight=weight
                covid_obj.pulse=pulse
                covid_obj.blood_pressure=blood_pressure
                covid_obj.temprature=temprature
                covid_obj.spo2=spo2
                covid_obj.symptoms=symptoms
                covid_obj.comorbidity_existing_disease=comorbidity_existing_disease
                covid_obj.save()              
                messages.info(request,"Data store Sucessfully.......")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    context = {
        'form': form,
        'covid_page': 'active',
        "company":cname
    }        
    return render(request, "websiteviews/covid19.html",context)





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





  