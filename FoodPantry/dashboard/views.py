from django.http import HttpResponse
from inventory.models import inventory
from inventory.forms import inventory_form
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def join(request):

    registered = False

    if request.method == 'POST':

        user_form = profile_form(data=request.POST)
   
        if user_form.is_valid(): 


            user = user_form.save()

   
            user.set_password(user.password)

   
            user.save()

            registered = True

        else:
    
            print(user_form.errors) 

    else:
        user_form = profile_form()

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

@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))
