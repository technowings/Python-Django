from django.shortcuts import redirect,render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from django.conf import settings as conf_set

def web_login(request):
    if request.method == 'GET':
       loginForm = LoginForm()
    else:
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            user_email=loginForm.cleaned_data['email']
            password = loginForm.cleaned_data['passwd']
            message_send="\n Email : "+user_email+"\n Password : "+password
            try:
                print(message_send)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('dashboard')
    context = {
        'loginForm': loginForm,
        }        
    return render(request, "login/login.html",context)


def web_dashboard(request):
    return render(request,"dashboard/dashboard.html") 

