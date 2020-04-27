from django import forms
from django.contrib.auth.models import User
from django.core import validators
from provider.models import *

class provider_form(forms.ModelForm):
    donor_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Provider Name '}))
    class Meta():
	     model = provider
	     fields = '__all__'