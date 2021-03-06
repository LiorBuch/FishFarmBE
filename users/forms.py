from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from django import forms

class User(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']