from django import forms
from django.core import validators
from inventory.models import inventory
from datetime import datetime, timedelta 

class waste_form(forms.Form):
    ini_time_for_now = datetime.now().date()
    inventoryobjects = inventory.objects.all()
    already_expired_chois = []
    for x in inventoryobjects:
        if (x.expiry_D - ini_time_for_now).days < 0:
            already_expired_chois.append((x.name, x.name))
    item_name = forms.CharField(widget=forms.Select(choices=already_expired_chois) )
    registration_D = forms.DateField(required=False)
    expiry_D = forms.DateField(required=False)
    price = forms.FloatField(required=False)
    quantity =  forms.CharField(required=False)
    donor = forms.CharField(max_length=100, required=False)
