from django.shortcuts import render
from django.http import HttpResponse
from checkout.models import checkout
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from dashboard.forms import *
from inventory.models import inventory
from datetime import datetime, timedelta
from provider.models import provider

# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
    dictOfCheckouts = getCheckOutInfo()
    dictOfPieChart = getPieChartInfo()
    total_donors = getDonorCount()
    mostdonatedItems = calculateDonations()
    DonorDetails = getDonorDetails()
    page_data = {"ChartData":dictOfCheckouts, "good_products":dictOfPieChart.get("total_good"), "about_to_expire":dictOfPieChart.get("about_to_expire"), "already_expired": dictOfPieChart.get("already_expired"), "total_donors": total_donors, "dat2":mostdonatedItems, "DonorDetails": DonorDetails}
    return render(request, "dashboard/dashboard.html", context=page_data)



def getDonorDetails():
    provider_list = provider.objects.all()
    countOfIndividual = 0
    countOfOrganization = 0
    countOfAnonymous = 0
    for j in provider_list:
        if j.anonymus_status == True:
            countOfAnonymous = countOfAnonymous + 1
        elif j.donor_status == 'Individual' and j.anonymus_status == False:
            countOfIndividual = countOfIndividual + 1
        elif j.donor_status == 'Organisation' and j.anonymus_status == False:
            countOfOrganization = countOfOrganization + 1
    return {"countOfIndividual": countOfIndividual, "countOfOrganization": countOfOrganization, "countOfAnonymous": countOfAnonymous}



def calculateDonations():

    page_data_chartist = {}
    page_data_chartist_ret = {}

    raw_data = inventory.objects.all()

    for x in raw_data:
        page_data_chartist.setdefault(x.name, 0)


    for x in raw_data:
        page_data_chartist[x.name] = x.quantity


    print(page_data_chartist)

    j = 0
    l1 = []
    l2 = []
    for w in sorted(page_data_chartist, key=page_data_chartist.get, reverse=True):
        page_data_chartist_ret[w] = page_data_chartist[w]
        if j == 10:
            break
        j = j + 1

    return page_data_chartist_ret




def getDonorCount():
    provider_objects = provider.objects.all()
    count = 0
    for x in provider_objects:
        count = count + 1
    return count



def getPieChartInfo():
    ini_time_for_now = datetime.now().date()
    about_to_expire = 0
    already_expired = 0
    total = 0
    inventoryobjects = inventory.objects.all()
    for x in inventoryobjects:
        total = total + 1
        if (x.expiry_D - ini_time_for_now).days <= 2 and (x.expiry_D - ini_time_for_now).days >= 0:
            about_to_expire = about_to_expire + 1
        if (x.expiry_D - ini_time_for_now).days < 0:
            already_expired = already_expired + 1

    total = total - about_to_expire - already_expired
    piechartdict = {"total_good":total, "about_to_expire": about_to_expire, "already_expired": already_expired}
    return piechartdict


def getCheckOutInfo():
    allcheckoutObj = checkout.objects.all()
    chart_data = {}
    chart_data_updated = {}
    dateset = set()

    for x in allcheckoutObj:
        dateset.add(x.checkout_date)

    for i in dateset:
        sum = 0
        for j in allcheckoutObj:
            if j.checkout_date == i:
                sum = sum + 1
        chart_data[i] = sum

    l = 0
    chart_data_sorted = sorted(chart_data, key = chart_data.get)
    for k in chart_data_sorted:
        print(k.strftime("%d %b %Y "), chart_data[k])
        chart_data_updated[k.strftime("%d %b %Y ")] = chart_data[k]
        if l == 10:
            break
        l = l + 1
    return chart_data_updated


def join(request):

    registered = False

    if request.method == 'POST':

        user_form = JoinForm(data=request.POST)
   
        if user_form.is_valid(): 


            user = user_form.save()

   
            user.set_password(user.password)

   
            user.save()

            registered = True

        else:
    
            print(user_form.errors) 

    else:
        user_form = JoinForm()

    context={'user_form':user_form,'registered':registered}
    return render(request,'dashboard/join.html', context)  


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:

                login(request,user)

                return HttpResponseRedirect(reverse('dashboard'))
            else:

                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:

        return render(request, 'dashboard/login.html', {})

@login_required(login_url='login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))
    
    
    
def about(request):
    return render(request, 'dashboard/About.html')
