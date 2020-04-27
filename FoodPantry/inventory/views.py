
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

def inventory_view(request):
	item = inventory.objects.all()
		
	item_data = inventory_form()
	if (request.method=="POST"):
			item_data = inventory_form(request.POST)
	if item_data.is_valid():
			item_data.save()

	context = {'item':item,'item_data':item_data}
	return render(request, 'inventory/inventory.html',context)


def update(request, pk):
	item = inventory.objects.get(id=pk)

	form = inventory_form(instance=item)

	if request.method == 'POST':
		form = inventory_form(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('inventory_view')

	context = {'form':form}

	return render(request, 'inventory/update.html', context)


def remove(request):
		item_id = request.GET['id']  
		item = inventory.objects.get(id=item_id)
		item.delete()
		return redirect('inventory_view')
		context={'item':item}
		return render(request, 'inventory/inventory.html',context)