from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import auth, messages

def index(request):
    return render(request, 'index.html')


def register(request):
   if request.method == 'POST':
       username = request.POST['username']
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       email = request.POST['email']
       password = request.POST['password']
       confirm_pass = request.POST['confirm_pass'] 

       user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password, )
       user.save()
       print('saved')
       return redirect('/')

   else:
       return render(request, 'Register.html')

def Login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user :
            if user.is_active:
                auth.login(request, user)
                messages.success(request, 'you have succesfull Login ' + username)
                return redirect ('/register')

            else:
                messages.error(request, 'invalid details')
                return render(request, 'login.html')

        else:
            messages.warning(request, 'please register here')
            return render(request, 'Register.html')

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {"form":form})

def logout_request(request):
    auth.logout(request)
    return redirect ('/')

# Create your views here.