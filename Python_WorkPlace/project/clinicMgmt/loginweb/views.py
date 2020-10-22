from django.shortcuts import redirect,render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from loginweb.forms import LoginForm,RegisterForm,PRegistrationForm,PrecForm
from django.conf import settings as conf_set
from django.contrib import messages
from django.contrib.auth.models import User,auth
from website.models import Appointment,Covid19
from loginweb.models import PatientRegister,PatientPrec
import xlwt
from xlwt.Formatting import Borders
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from datetime import date


cname=conf_set.CNAME


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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def web_dashboard(request):
    if request.session.has_key('username'):
        cname=conf_set.CNAME
        user_name=request.session['username']
        #x=str(datetime.date.now())
        today = date.today() 
        print(today)
        appoint = Appointment.objects.filter(appointment_date=today).count()
        covid= Covid19.objects.filter(date_of_checkup=today).count()
        context = {
            'company':cname,
            'user':user_name,
            'page_title':"Dashboard",
            "appoint":appoint,
            "covid":covid
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
        appoint=Appointment.objects.all()
        context = {
            'company':cname,
            'user':user_name,
            'page_title':"Appointments",
            'appoint':appoint
            }
        return render(request,"drviews/appointment.html",context)  
    else:
        return redirect('login')

def admin_covid19(request):
    if request.session.has_key('username'):
        cname=conf_set.CNAME
        user_name=request.session['username']  
        covid=Covid19.objects.all()      
        context={'company':cname,
            'user':user_name,
            'page_title':"Covid19",
            "covid":covid
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
            pregisterForm=PRegistrationForm(request.POST,request.FILES)
            if pregisterForm.is_valid():
                try:
                    patient=PatientRegister()
                    patient.email=pregisterForm.cleaned_data['PR_email']
                    patient.fname=pregisterForm.cleaned_data['PR_firstname']
                    patient.lname=pregisterForm.cleaned_data['PR_lastname']
                    patient.mobile=pregisterForm.cleaned_data['PR_mobile']
                    patient.address=pregisterForm.cleaned_data['PR_address']
                    patient.phto=pregisterForm.cleaned_data['PR_photo']
                    patient.dob=pregisterForm.cleaned_data['PR_dob']
                    patient.sex=pregisterForm.cleaned_data['PR_sex']
                    patient.save()
                    
                    return redirect('admin_pregister')
                except:
                    return HttpResponse('Invalid header found. here...')
                #return redirect('register')   
    pregisterdata=PatientRegister.objects.all()
    context = {
        'pregisterForm': pregisterForm,'company':cname,'user':user_name,'page_title':"Patients Registration","pregisterdata":pregisterdata,}        
    return render(request, "drviews/registration.html",context)



def export_appointments_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="appointments.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Appointments')

    # Sheet header, first row
    row_num = 0

    excel_style = xlwt.XFStyle()
    excel_style.font.bold = True
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    excel_style.borders = borders
    columns = ['Name', 'Dob', 'Gender', 'Appointment_date','Appointment_session','Mobile','Message', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], excel_style)

    # Sheet body, remaining rows
    excel_style = xlwt.XFStyle()
    excel_style.borders = borders
    rows = Appointment.objects.all().values_list('name', 'dob', 'gender', 'appointment_date','appointment_session','mobile','message')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], excel_style)

    wb.save(response)
    return response







def change_pass(request):
    if request.session.has_key('username'):
        lname=request.user.first_name 
        fname=request.user.first_name
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password has been changed successfully!')
                return redirect('change_password')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        context = {
            
            'lname':lname,
            'fname':fname,
             "form":form
            }    
        return render(request, 'drviews/changepass.html',context) 
    else:
        return redirect('login')  



def admin_history(request):
    if request.session.has_key('username'):
        cname=conf_set.CNAME
        user_name=request.session['username']
        pregisterdata=PatientRegister.objects.all()
        context = {
            'company':cname,
            'user':user_name,
            'page_title':"Appointments",
            'pregisterdata':pregisterdata
            }
        return render(request,"drviews/history.html",context) 
    else:
        return redirect('login')

    


def admin_addPrec(request):
    if request.session.has_key('username'):
        cname=conf_set.CNAME
        user_name=request.session['username']
        if request.method=='GET':
            precform=PrecForm()
        else:
            precform=PrecForm(request.POST)
            precmodel=PatientPrec()
            if precform.is_valid():
               precmodel.prec=precform.cleaned_data['prec']
               #precmodel.patient=precform.cleaned_data['prec']
               precmodel.save()
               messages.success(request, 'Precription save sucessfully!')
              

        context = {
            'company':cname,
            'user':user_name,
            'page_title':"Add Precription",
            'precform':precform
            }
        return render(request,"drviews/prec_add.html",context)
    else:
        return redirect('login')
   



def admin_prescr(request):
    if request.session.has_key('username'):
        cname=conf_set.CNAME
        user_name=request.session['username']
        pregisterdata=PatientRegister.objects.all()
        context = {
            'company':cname,
            'user':user_name,
            'page_title':"Precription",
            'pregisterdata':pregisterdata
            }
        return render(request,"drviews/precription.html",context) 
    else:
        return redirect('login')
    