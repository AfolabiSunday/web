from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

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
    return render(request, 'login.html')

# Create your views here.