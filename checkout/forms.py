from django import forms
from django.contrib.auth.models import User
from django.core import validators
from checkout.models import *
from inventory.models import inventory
from datetime import datetime, timedelta 

class checkout_form(forms.ModelForm):
    student_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Student ID '}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Quantity '}))
    item_name = forms.CharField(required=False)
    price = forms.FloatField(required=False)
    donor = forms.CharField(required=False)
    def findOptions():
        inventory_objects = inventory.objects.all()
        ini_time_for_now = datetime.now().date()
        myList = []
        for x in inventory_objects:
            if x.expiry_D >= ini_time_for_now:
                myList.append((x.name, x.name))
        return myList
    CHS = findOptions()
    item_in_inventory = forms.CharField(widget=forms.Select(attrs={'style':'display:inline;'},choices=CHS))
    class Meta():
	     model = checkout
	     fields = '__all__'


  