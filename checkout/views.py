from checkout.models import *
from checkout.forms import *
from checkout.models import *
from checkout.forms import *
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def checkout_view(request):
		cout = checkout.objects.all()
		cout_data = checkout_form()

		if (request.method=="POST"):
			cout_data = checkout_form(request.POST)
			if cout_data.is_valid():
				a1 = cout_data.cleaned_data["item_in_inventory"]
				after = cout_data.cleaned_data["quantity"]
				x = inventory.objects.get(name=a1)
				before = x.quantity
				final = int(before) - int(after)
				if final < 0:
				   print("Not enough items in inventory")
				else:
					x.quantity = final
					x.save()
					cout_data.save()
		context = {'cout':cout,'cout_data':cout_data}
		return render(request, "checkout/checkout.html",context)

def update_co(request, pk):
		item = checkout.objects.get(id=pk)

		form = checkout_form(instance=item)

		if request.method == 'POST':
			form = checkout_form(request.POST, instance=item)
			if form.is_valid():
					a1 = form.cleaned_data["item_in_inventory"]
					after = form.cleaned_data["quantity"]
					x = inventory.objects.get(name=a1)
					before = x.quantity
					final = int(before) - int(after)
					if final < 0:
					   print("Not enough items in inventory")
					else:
						x.quantity = final
						x.save()
						form.save()
						return redirect('checkout_view')

		context = {'form':form}

		return render(request, 'checkout/update_co.html', context)


def remove_co(request):
		item_id = request.GET['id']  
		item = checkout.objects.get(id=item_id)
		item.delete()
		return redirect('checkout_view')
		context={'item':item}
		return render(request, 'checkout/checkout.html',context)