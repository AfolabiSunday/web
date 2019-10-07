from .models import *
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model = new_user
        fields = ['username', 'firstname', 'lastname', 'email']
