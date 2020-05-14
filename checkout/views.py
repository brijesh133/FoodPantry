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
from checkout.serializers import *
from rest_framework import viewsets
from rest_framework import permissions

class CheckoutViewSet(viewsets.ModelViewSet):
 queryset = checkout.objects.all()
 serializer_class = CheckoutSerializer
 permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):

 queryset = User.objects.all()
 serializer_class = UserSerializer
 permission_classes = [permissions.IsAuthenticated]
# Create your views here.
@login_required(login_url='/login/')
def checkout_view(request):
		cout_data = checkout_form()
		isInserted = False
		if (request.method=="POST"):
			cout_data = checkout_form(request.POST)
			if cout_data.is_valid():
				a1 = cout_data.cleaned_data["item_in_inventory"]
				after = cout_data.cleaned_data["quantity"]
				student_ids = cout_data.cleaned_data["student_id"]
				x = inventory.objects.filter(name=a1)[0]
				before = x.quantity
				final = int(before) - int(after)
				if final < 0:
				   return render(request, "dashboard/Error.html")
				else:
					x.quantity = final
					y = checkout()
					y.item_in_inventory = a1
					y.item_name = a1
					y.student_id = student_ids
					y.quantity = after
					y.price = float(after) * x.price
					y.donor = x.donor
					y.save()
					isInserted = True
					print("isInserted: ",isInserted)
					if final == 0:
						x.delete()
					else:
						x.save()
		cout = checkout.objects.all()
		context = {'cout':cout,'cout_data':cout_data, 'isInserted':isInserted}
		return render(request, "checkout/checkout.html",context)