from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages, auth

from django.urls import path
from banking_app import views
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('view')
        else:
            messages.info(request,'invalid username and password')
            return redirect('login')
    return render(request,'login.html')

def view(request):
    return render(request,'view.html')
def form(request):

    return render(request,'form.html')
def application(request):
    return render(request,'application.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                    messages.info(request, "username taken")
                    return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
