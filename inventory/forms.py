from django import forms
from django.contrib.auth.models import User
from django.core import validators
from inventory.models import *

class inventory_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Item Name '}))
    expiry_D = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Expiry Date '}))
    price = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Price'}))
    quantity  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Quantity '}))

    class Meta():
	     model = inventory
	     fields = '__all__'

class profile_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
      model = User
      fields = ('first_name','last_name','username','email','password')