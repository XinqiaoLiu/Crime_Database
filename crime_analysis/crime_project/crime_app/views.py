from django.shortcuts import render
from django.http import HttpResponse
from .models import district
from django.http import Http404
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def insert_district(request):
    if request.method=='POST':
        if request.POST.get("Neighborhood") and request.POST.get("Population") and request.POST.get("Home_Value") and request.POST.get("Median_Income"):
            d = district()
            d.Neighborhood = request.POST.get("Neighborhood")
            d.Population = request.POST.get("Population")
            d.Home_Value = request.POST.get("Home_Value")
            d.Median_Income = request.POST.get("Median_Income")
            d.save()
            return render(request, 'crime_app/district.html')
        else:
            Http404("info not complete")
    else:
        return render(request,'crime_app/district.html')
