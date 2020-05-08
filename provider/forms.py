from django import forms
from django.contrib.auth.models import User
from django.core import validators
from provider.models import *

class provider_form(forms.ModelForm):
    donor_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Provider Username'}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Provider Name'}))
    CHS = [('Individual', 'Individual'), ('Organisation', 'Organisation')]
    donor_status = forms.CharField(widget=forms.Select(attrs={'style':'display:inline;'},choices=CHS))
    class Meta():
	     model = provider
	     fields = '__all__'


class update_form(forms.Form):
    donor_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Provider Name'}))
    CHS = [('Individual', 'Individual'), ('Organisation', 'Organisation')]
    donor_status = forms.CharField(widget=forms.Select(attrs={'style':'display:inline;'},choices=CHS))
