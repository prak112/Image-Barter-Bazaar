from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import UserProfile


class RegForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "email", "user_type", "bio", "username"]
    

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "email", "user_type", "bio", "username"]
