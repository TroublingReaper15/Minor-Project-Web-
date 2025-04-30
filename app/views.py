from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request,'index.html')

def shop(request):
    return render(request, 'shop.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def register(request):
    return render(request, 'register.html')

def registeration(request):
    user_name=request.POST.get('name')
    user_email=request.POST.get('username')
    user_password=request.POST.get('password')
    user_data=User.objects.create(name=user_name,username=user_email, password=user_password)
    return render(request, 'login.html')

def log(request):
    user_email=request.POST.get('username')
    user_password=request.POST.get('password')
    user_data=User.objects.filter(username=user_email)
    if user_data:
        data=User.objects.get(username=user_email)
        p=data.name
        q=data.username
        r=data.password
        s=data.id
        login_data={'p':p,'q':q,'r':r,'s':s}
        if user_password==r:
            return render(request, 'index.html', {'login_data':login_data})
        else:
            return render(request, 'login.html', {'error': 'Invalid Password !!!'})
    else:
        return render(request, 'login.html', {'error': 'Invalid Username !!!'})