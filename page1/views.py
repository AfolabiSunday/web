from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import auth, messages

def index(request):
    return render(request, 'index.html')


def register(request):
   if request.method == 'POST':
       form = LoginForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect ('/')
   else:
        form = LoginForm()
   return render (request, 'Register.html', {'form':form})

def Login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        form.is_valid()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you have succesfull Login ' + username)
            return redirect ('/register')

        else:
            messages.error(request, 'invalid details')
            return render(request, 'login.html')

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {"form":form})

def logout_request(request):
    auth.logout(request)
    return redirect ('/')

# Create your views here.