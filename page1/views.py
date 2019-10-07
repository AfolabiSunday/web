from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

from django.contrib import auth

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

def Login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username','')
        user_password = request.POST.get('pass', '')

        user = auth.authenticate(request, username=user_name, password=pass_word)
        if user is not None:
            auth.login(request, user)
            return redirect ('/')

        else:
            error_json = {'error_message': 'User name or password is not correct.'}
            return render(request, 'login.html', error_json)

    else:
        return render(request, 'login.html')

def loginSuccess(request):
   pass

# Create your views here.