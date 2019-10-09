from .models import *
from django import forms

class LoginForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = new_user
        fields = ['username', 'password', 'firstname', 'lastname', 'email']


