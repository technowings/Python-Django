from django.shortcuts import redirect,render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from loginweb.forms import LoginForm,RegisterForm,PRegistrationForm
from django.conf import settings as conf_set
from django.contrib import messages
from django.contrib.auth.models import User,auth

def web_register(request):
    cname=conf_set.CNAME
    if request.method=='GET':
        registerForm=RegisterForm()
    else:
        registerForm=RegisterForm(request.POST)
        if registerForm.is_valid():
            user_name=registerForm.cleaned_data['usrR_name']
            user_email=registerForm.cleaned_data['usrR_email']
            user_fistname=registerForm.cleaned_data['usrR_firstname']
            user_lastname=registerForm.cleaned_data['usrR_lastname']
            user_password=registerForm.cleaned_data['usrR_passwd']
            user_password2=registerForm.cleaned_data['usrR_passwd2']
            try:
                if (user_password==user_password2):
                    if User.objects.filter(username=user_name).exists():
                        messages.warning(request,'User name exists... try another')
                        return redirect('register') 
                    elif User.objects.filter(email=user_email).exists(): 
                        messages.warning(request,'User email exists... try another') 
                        return redirect('register')    
                    else:
                        user=User.objects.create_user(username=user_name,email=user_email,password=user_password,first_name=user_fistname,last_name=user_lastname)
                        user.save() 
                        messages.warning(request,'User email exists... try another') 
                        messages.success(request,'User Created Sucessfully...')
                        return redirect('register') 
                else:
                    messages.info(request,'Password not matching.... try again') 
                    return redirect('register')    
            except:
                return HttpResponse('Invalid header found. here...')
                #return redirect('register')   

    context = {
        'registerForm': registerForm,'company':cname,
        }        
    return render(request, "login/register.html",context)


def web_login(request):
    cname=conf_set.CNAME
    if request.method=='GET':
        loginForm=LoginForm()
    else:
        loginForm=LoginForm(request.POST)    
        if loginForm.is_valid():
            userName=loginForm.cleaned_data['username']
            userPassword=loginForm.cleaned_data['passwd']
            try:
                user=auth.authenticate(username=userName,password=userPassword)
                if user is not None:
                    auth.login(request,user)
                    request.session['username']=userName
                    return redirect('dashboard')
                else:
                    messages.error(request,'invalid Credi.... try again')    
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            #return redirect('dashboard') 
    context = {
        'loginForm': loginForm,'company':cname,
        }        
    return render(request, "login/login.html",context)  


def web_dashboard(request):
    if request.session.has_key('username'):
        cname=conf_set.CNAME
        user_name=request.session['username']
        context = {
            'company':cname,
            'user':user_name,
            'page_title':"Dashboard"
            }
        return render(request,"drviews/dashboard.html",context) 
    else:
        return redirect('login') 

def web_logout(request):
    del request.session['username']
    auth.logout(request)
    return redirect('login')

def admin_appointment(request):
    if request.session.has_key('username'):
        cname=conf_set.CNAME
        user_name=request.session['username']
        context = {
            'company':cname,
            'user':user_name,
            'page_title':"Appointments"
            }
        return render(request,"drviews/appointment.html",context)  
    else:
        return redirect('login')

def admin_covid19(request):
    if request.session.has_key('username'):
        cname=conf_set.CNAME
        user_name=request.session['username']        
        context={'company':cname,
            'user':user_name,
            'page_title':"Covid19"
            }
        return render(request,"drviews/covid19.html",context)
    else:
        return redirect('login')  

def admin_Pregister(request):
    if request.session.has_key('username'):
        cname=conf_set.CNAME
        user_name=request.session['username'] 
        if request.method=='GET':
            pregisterForm=PRegistrationForm()
        else:
            pregisterForm=PRegistrationForm(request.POST)
            if pregisterForm.is_valid():
                user_email=pregisterForm.cleaned_data['PR_email']
                user_fistname=pregisterForm.cleaned_data['PR_firstname']
                user_lastname=pregisterForm.cleaned_data['PR_lastname']
                try:
                    pass
                except:
                    return HttpResponse('Invalid header found. here...')
                #return redirect('register')   

    context = {
        'pregisterForm': pregisterForm,'company':cname,'user':user_name,'page_title':"Patients Registration"
        }        
    return render(request, "drviews/registration.html",context)





