from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ExtendedUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = ExtendedUser
        fields = ['username', 'email', 'choice', 'password1', 'password2']
