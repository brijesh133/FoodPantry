from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from inventory.models import inventory
from datetime import datetime, timedelta 
# Create your views here.

def waste_reduction(request):
    ini_time_for_now = datetime.now().date()
    print("Initial date: ", str(ini_time_for_now))
    future_date_after_2days = ini_time_for_now + timedelta(days = 2)
    print("future_date_after_2days: ", str(future_date_after_2days))
    about_to_expire = []
    inventoryobjects = inventory.objects.all()
    for x in inventoryobjects:
        print("Here")
        if x.expiry_D == future_date_after_2days:
            print("x.expiry_D", x.expiry_D)
            print("future_date_after_2days", future_date_after_2days)
            about_to_expire.append(x)
    page_data = {"expiring_soon" : about_to_expire}
    return render(request, "waste_reduction/waste.html", context=page_data)

