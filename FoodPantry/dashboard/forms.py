from django import forms
from django.contrib.auth.models import User
from django.core import validators
from inventory.models import *


class profile_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
      model = User
      fields = ('first_name','last_name','username','email','password')
