from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def waste_reduction(request):
	return render(request, "waste_reduction/waste.html")

