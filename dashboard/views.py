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
# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
    dictOfCheckouts = getCheckOutInfo()
    print(dictOfCheckouts)
    page_data = {"ChartData":dictOfCheckouts}
    return render(request, "dashboard/dashboard.html", context=page_data)




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