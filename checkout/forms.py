from django import forms
from django.contrib.auth.models import User
from django.core import validators
from checkout.models import *

class checkout_form(forms.ModelForm):
    student_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Student ID '}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Quantity '}))
    item_name = forms.CharField(required=False)
    price = forms.FloatField(required=False)
    donor = forms.CharField(required=False)
    class Meta():
	     model = checkout
	     fields = '__all__'