from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate ,login,logout
from django.contrib.messages import *
from django.contrib.auth.decorators import login_required
import logging
logger=logging.getLogger('django')

# Create your views here.

def sign_up(request):
    if request.method =='POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if name and email and password1 and password2:
            if password1 == password2:
                password=make_password(password1)
                user=User(username=name,email=email,password=password)
                user.save()
                return redirect("login_page")
   
    return render(request ,'home.html')

def login_page(request):
    try:
        if request.method =="POST":
            name = request.POST.get('username')
            password = request.POST.get('password1')
            print(name,password)
            user = authenticate(username=name,password=password)
            if user is not None:
                login(request,user)
                logger.info(msg='logged in now')
                return redirect("details")
            else:
                messages.info(request , "username or password is not match")
                return render(request,'login_page.html')
    except Exception as e :
        print('hello',e)

    return render(request,'login_page.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        logger.info(msg='logged out now')
    return redirect("login_page")

@login_required(login_url="login_page")
def details(request):
    
    return render(request,'details.html')