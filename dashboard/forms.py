from django import forms
from django.contrib.auth.models import User
from django.core import validators
from dashboard.models import *

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget= forms.TextInput
                           (attrs={'placeholder':'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    class Meta():
         model = profile
         fields = '__all__'
class JoinForm(forms.ModelForm):
    
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder':'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder':'Last Name'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder':'Username'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder':'Password'}))

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

   