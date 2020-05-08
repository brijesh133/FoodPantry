from django.shortcuts import render,redirect
from django.http import HttpResponse
from provider.models import *
from provider.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/')
def provider_view(request):
    donor = provider.objects.all()
        
    donor_data = provider_form()
    if (request.method=="POST"):
            donor_data = provider_form(request.POST)
    if donor_data.is_valid():
            name = donor_data.cleaned_data["donor_name"]
            d_status = donor_data.cleaned_data["donor_status"]
            u_name = donor_data.cleaned_data["user_name"]
            newProvider = provider()
            newProvider.donor_name = name
            newProvider.donor_status = d_status
            newProvider.user_name = u_name
            newProvider.save()


    context = {'donor':donor,'donor_data':donor_data}
    return render(request, 'provider/provider.html',context)

@login_required(login_url='/login/')
def update_pro(request, pk):
    donor = provider.objects.get(donor_name=pk)
    print("pk: ", pk)
    print("why1: ", donor)
    initial_dict = {"donor_name":donor.donor_name,"donor_status":donor.donor_status, "user_name": donor.user_name}
    print("initial_dict:", initial_dict)
    form_edit = update_form(initial=initial_dict)
    if request.method == 'POST':
        form = update_form(request.POST)
        print("why2: ", form)
        print("why3: ", form.is_valid())
        if form.is_valid():
            donor_user = form.cleaned_data["user_name"]
            donor_status1 = form.cleaned_data["donor_status"]
            print("why3: ")
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
    print("I am here in delete")
    donor_id = request.GET['name']
    print("donor_id: ", donor_id)  
    donor = provider.objects.get(donor_name=donor_id)
    print("Donor is here: ", donor)
    donor.delete()
    #return redirect('provider_view')
    context={'donor':donor}
    return redirect('provider_view')