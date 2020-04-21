from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def provider(request):
	return HttpResponse("Provider Page")

