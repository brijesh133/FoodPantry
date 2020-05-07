from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from inventory.models import inventory
from datetime import datetime, timedelta 
from waste_reduction.forms import waste_form
# Create your views here.

def waste_reduction(request):
    ini_time_for_now = datetime.now().date()
    print("Initial date: ", str(ini_time_for_now))
    future_date_after_2days = ini_time_for_now + timedelta(days = 2)
    waste_forms = waste_form()
    about_to_expire = []
    already_expired = []
    inventoryobjects = inventory.objects.all()
    for x in inventoryobjects:
        if (x.expiry_D - ini_time_for_now).days <= 2 and (x.expiry_D - ini_time_for_now).days >= 0:
            about_to_expire.append(x)
        if (x.expiry_D - ini_time_for_now).days < 0:
            already_expired.append(x)

    page_data = {"expiring_soon" : about_to_expire, "already_expired":already_expired, "waste_forms":waste_forms}
    return render(request, "waste_reduction/waste.html", context=page_data)




def waste_remove(request):
    print("Here")
    return redirect('waste')