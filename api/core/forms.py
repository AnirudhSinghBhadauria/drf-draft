from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
          'email', 'first_name', 'last_name', 'role', 
          'authorization'
        )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
          'email', 'password', 'first_name', 'last_name', 'role', 
          'authorization'
        )