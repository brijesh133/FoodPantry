from django.shortcuts import render,redirect
from django.http import HttpResponse
from provider.models import *
from provider.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from provider.serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from inventory.models import inventory
from checkout.models import checkout

class ProviderViewSet(viewsets.ModelViewSet):
 queryset = provider.objects.all()
 serializer_class = ProviderSerializer
 permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):

 queryset = User.objects.all()
 serializer_class = UserSerializer
 permission_classes = [permissions.IsAuthenticated]
# Create your views here.
@login_required(login_url='/login/')
def provider_view(request):
    donor = provider.objects.all()
        
    donor_data = provider_form()
    if (request.method=="POST"):
            donor_data = provider_form(request.POST)
            print("donor_data.is_valid(): ", donor_data.is_valid())     
    if donor_data.is_valid():
            name = donor_data.cleaned_data["donor_name"]
            d_status = donor_data.cleaned_data["donor_status"]
            u_name = donor_data.cleaned_data["user_name"]
            a_status = donor_data.cleaned_data["anonymus_status"]
            print("I am here in provider")
            checkExists = CheckIfExists(name)
            if checkExists:
                return HttpResponse("Username already exists, try with different username!")
            else:
                newProvider = provider()
                newProvider.donor_name = name
                newProvider.donor_status = d_status
                newProvider.user_name = u_name
                newProvider.anonymus_status = a_status
                newProvider.save()


    context = {'donor':donor,'donor_data':donor_data}
    return render(request, 'provider/provider.html',context)





def details(request,pk):
    donor_details = provider.objects.get(donor_name=pk)
    inventory_details = inventory.objects.filter(donor=pk)
    print("inventory_details", inventory_details)
    checkout_details = checkout.objects.filter(donor=pk)
    print("checkout_details", checkout_details)
    context = {"donor_details": donor_details}
    return render(request, 'provider/Details.html', context)


















def CheckIfExists(u_name):
    provider_objects = provider.objects.all()
    for x in provider_objects:
        if x.donor_name == u_name:
            return True
    return False






@login_required(login_url='/login/')
def update_pro(request, pk):
    donor = provider.objects.get(donor_name=pk)
    initial_dict = {"donor_name":donor.donor_name,"donor_status":donor.donor_status, "user_name": donor.user_name, "anonymus_status" : donor.anonymus_status}
    form_edit = update_form(initial=initial_dict)
    if request.method == 'POST':
        form = update_form(request.POST)
        if form.is_valid():
            donor_user = form.cleaned_data["user_name"]
            donor_status1 = form.cleaned_data["donor_status"]
            donor.user_name = donor_user
            donor.donor_status = donor_status1
            donor.save()
            donor_obj = provider.objects.all()
            donor_data = provider_form()
            context = {'donor':donor_obj,'donor_data':donor_data}
            return render(request, 'provider/provider.html', context)
    		

    context = {'form':form_edit}
    return render(request, 'provider/update_pro.html', context)


def remove_pro(request):
    donor_id = request.GET['name']
    donor = provider.objects.get(donor_name=donor_id)
    donor.delete()
    context={'donor':donor}
    return redirect('provider_view')