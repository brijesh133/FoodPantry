from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def checkout(request):
	return render(request, "checkout/checkout.html")

