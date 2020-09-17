from django.shortcuts import render

def home_page(request):
    return render(request,'index.html')

def serv_page(request):
    return render(request,'srve.html')

# Create your views here.
