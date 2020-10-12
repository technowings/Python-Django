from django.shortcuts import render
from .models import VTServices
from .models import VTAbout
from .models import VTPortfolioMob,VTPortfolioIot,VTPortfolioWeb
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


cname="Bodhi Technology"
caddress="216,Settelment Free Colony,Solapur, Maharashtra-413001 INDIA "
cemail="bodhi.technology@outlook.com"
cmobil="+91-8007915552"
cgmap="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1900.9729079187462!2d75.88880177168748!3d17.652725147121007!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTfCsDM5JzA5LjgiTiA3NcKwNTMnMjMuMCJF!5e0!3m2!1sen!2sin!4v1584424575512!5m2!1sen!2sin"
cabout="is a leading software development company providing software consultancy and solutions to Industries and educational Institutes.We are one stop shop for all kinds of customized softwares and automation required."
cabout1="providing complete suite of software solutions and services that meet their evolving needs and growing business ,the most sophisticated and yet user-friendly software to use."

def home(request):
    
    vtservs=VTServices.objects.all()
     
    vtabouts=VTAbout.objects.all()
    
    vtprotfoliMob=VTPortfolioMob.objects.all()
  
    vtprotfoliIot=VTPortfolioIot.objects.all()
    
    vtportfoliWeb=VTPortfolioWeb.objects.all()

    
   
    # homelist={'vtservs':vtservs,'cemail':cemail,'cname':cname,'cmobil':cmobil,'caddress':caddress,'cgmap':cgmap,'cabout':cabout,'cabout1':cabout1,'vtabouts':vtabouts,'vtprotfoliMob':vtprotfoliMob,'vtprotfoliIot':vtprotfoliIot,'vtportfoliWeb':vtportfoliWeb,'feedback':feedback}

       
    return render(request,'index.html',{'vtservs':vtservs,'cemail':cemail,'cname':cname,'cmobil':cmobil,'caddress':caddress,'cgmap':cgmap,'cabout':cabout,'cabout1':cabout1,'vtabouts':vtabouts,'vtprotfoliMob':vtprotfoliMob,'vtprotfoliIot':vtprotfoliIot,'vtportfoliWeb':vtportfoliWeb })

# Create your views here.

def send_email(request):
    person_name=request.POST.get('name', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message','')
    from_email = request.POST.get('email', '')
    
    if subject and message and from_email and person_name:
        try:
            send_mail(subject,message,from_email, ['bodhi.technology@outlook.com'])
            print(person_name)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Your message has been sent. Thank you!')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

