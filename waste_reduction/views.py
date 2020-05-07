from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from inventory.models import inventory
from datetime import datetime, timedelta 
from waste_reduction.forms import waste_form
from waste_reduction.models import wastage
# Create your views here.

@login_required(login_url='/login/')
def waste_reduction(request):
    ini_time_for_now = datetime.now().date()
    print("Initial date: ", str(ini_time_for_now))
    future_date_after_2days = ini_time_for_now + timedelta(days = 2)
    gotmyList = getmyList()
    waste_forms = waste_form()
    about_to_expire = []
    already_expired = []
    inventoryobjects = inventory.objects.all()
    for x in inventoryobjects:
        print(x.registration_D)
        if (x.expiry_D - ini_time_for_now).days <= 2 and (x.expiry_D - ini_time_for_now).days >= 0:
            about_to_expire.append(x)
        if (x.expiry_D - ini_time_for_now).days < 0:
            already_expired.append(x)

    page_data = {"expiring_soon" : about_to_expire, "already_expired":already_expired, "waste_forms":waste_forms}
    return render(request, "waste_reduction/waste.html", context=page_data)


def getmyList():
    ini_time_for_now = datetime.now().date()
    inventoryobjects = inventory.objects.all()
    already_expired_chois = []
    for x in inventoryobjects:
        if (x.expiry_D - ini_time_for_now).days < 0:
            already_expired_chois.append((x.id, x.name))
    return already_expired_chois

def waste_remove(request):
    if(request.method == "POST"):
        form_data = waste_form(request.POST)
        print("form_data.is_valid()",form_data.is_valid())
        if form_data.is_valid():
            print("Inside data is correct")
            item = form_data.cleaned_data["item_name"]
            print("item: ", item)
            inv_object = inventory.objects.get(id=item)
            print("inv_object: ",inv_object)
            quantity = form_data.cleaned_data["quantity"]
            registration_date = inv_object.registration_D
            expiry_date = inv_object.expiry_D
            price = inv_object.price
            donor = inv_object.donor
            
            if int(quantity) < inv_object.quantity:
                waste_object = wastage()
                waste_object.item_name = item
                waste_object.registration_D = registration_date
                waste_object.expiry_D = expiry_date
                waste_object.price = price
                waste_object.quantity = int(quantity)
                waste_object.donor = donor
                waste_object.save()
                inv_object.quantity = inv_object.quantity - int(quantity)
                inv_object.save()
            else:
                waste_object = wastage()
                waste_object.item_name = item
                waste_object.registration_D = registration_date
                waste_object.expiry_D = expiry_date
                waste_object.price = price
                waste_object.quantity = int(quantity)
                waste_object.donor = donor
                waste_object.save()
                inv_object.quantity = inv_object.quantity - int(quantity)
                inv_object.delete()
    print("Here")
    return redirect('waste')