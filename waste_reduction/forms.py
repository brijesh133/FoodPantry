from django import forms
from django.core import validators
from inventory.models import inventory
from datetime import datetime, timedelta 

class waste_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super(waste_form, self).__init__(*args, **kwargs)
        
        ini_time_for_now = datetime.now().date()
        inventoryobjects = inventory.objects.all()
        already_expired_chois = []
        for x in inventoryobjects:
            if (x.expiry_D - ini_time_for_now).days < 0:
                already_expired_chois.append((x.id, x.name))

        self.fields['item_name'] = forms.CharField(widget=forms.Select(choices=already_expired_chois) )
        self.fields['registration_D'] = forms.DateField(required=False)
        self.fields['expiry_D'] = forms.DateField(required=False)
        self.fields['price'] = forms.FloatField(required=False)
        self.fields['quantity'] =  forms.CharField(required=False)
        self.fields['donor'] = forms.CharField(max_length=100, required=False)
