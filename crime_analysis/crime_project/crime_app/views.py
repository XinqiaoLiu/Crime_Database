from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import district
from django.http import Http404
from django.contrib import messages
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
            return render(request, 'crime_app/insert_district.html',{'d':d})
    return render(request,'crime_app/insert_district.html',{'incomplete':"You must enter all the info to insert"})

def search_district(request):
    if request.method=='GET':
        d_name = request.GET.get("Neighborhood")
        if d_name is not None:
            try:
                d = district.objects.get(pk=d_name)
            except district.DoesNotExist:
                return render(request,'crime_app/search_district.html',{'dne':"Neighborhood does not exist"})
            return render(request, 'crime_app/search_district.html',{'d':d})

    return render(request, 'crime_app/search_district.html')

def update_district(request):
    if request.method=='POST':
        d_name = request.POST.get("Neighborhood")

        if d_name is not None:
            d = district.objects.get(pk=d_name)
            if request.POST.get("Population"):
                d.Population = request.POST.get("Population")
            if request.POST.get("Home_Value"):
                d.Home_Value = request.POST.get("Home_Value")
            if request.POST.get("Median_Income"):
                d.Median_Income = request.POST.get("Median_Income")
            d.save()
            return render(request, 'crime_app/update_district.html',{'d':d})
    return render(request, 'crime_app/update_district.html')

def delete_district(request):
        if request.method=='POST':
            d_name = request.POST.get("Neighborhood")
            if d_name is not None:
                district.objects.filter(pk=d_name).delete()
                return render(request, 'crime_app/delete_district.html',{'d_name':d_name})

        return render(request, 'crime_app/delete_district.html')

def main_page(request):
    return render(request,'crime_app/main.html')
