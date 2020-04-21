from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def impact_measurement(request):
	return HttpResponse("Impact Measurement Page")

