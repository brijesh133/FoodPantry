from django.shortcuts import render,redirect
from django.http import HttpResponse
from provider.models import *
from provider.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def provider_view(request):
	donor = provider.objects.all()
		
	donor_data = provider_form()
	if (request.method=="POST"):
			donor_data = provider_form(request.POST)
	if donor_data.is_valid():
			donor_data.save()

	context = {'donor':donor,'donor_data':donor_data}
	return render(request, 'provider/provider.html',context)

def update_pro(request, pk):
	donor = provider.objects.get(id=pk)

	form = provider_form(instance=donor)

	if request.method == 'POST':
		form = provider_form(request.POST, instance=donor)
		if form.is_valid():
			form.save()
			return redirect('provider_view')

	context = {'form':form}

	return render(request, 'provider/update_pro.html', context)


def remove_pro(request):
		donor_id = request.GET['id']  
		donor = provider.objects.get(id=donor_id)
		donor.delete()
		return redirect('provider_view')
		context={'donor':donor}
		return render(request, 'provider/provider.html',context)