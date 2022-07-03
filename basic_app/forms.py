from dataclasses import fields
from importlib.metadata import files
from django import forms
from django.contrib.auth.models import User
from .models import UserProfileModel



class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForms(forms.ModelForm):
    class Meta():
        model = UserProfileModel
        fields = ('portfolio_site', 'profile_pic')
