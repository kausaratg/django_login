from dataclasses import fields
from importlib.metadata import files
from tkinter.tix import Tree
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfileModel



class UserForms(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'email', 'password1']
    def save(self, commit = True):
        user = super(UserForms, self).save(commit= False)
        if commit:
            user.save()
        return user


class UserProfileForms(forms.ModelForm):
    class Meta():
        model = UserProfileModel
        fields = ['portfolio_site', 'profile_pic']
