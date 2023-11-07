from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from users.models import UserProfile


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ["username", "password"]


class RegForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "email", "username", "password", "customer_type", "bio"]
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))