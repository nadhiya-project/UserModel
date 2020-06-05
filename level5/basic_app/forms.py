from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model=UserInfo
        fields=('portfolio','profile_pic')
