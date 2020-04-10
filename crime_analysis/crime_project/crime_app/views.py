from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import district, crime
from django.http import Http404
from django.contrib import messages
import datetime
# Create your views here.

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

def insert_crime(request):
    if request.method=='POST':
        if request.POST.get("ID") and request.POST.get("Type") and request.POST.get("Area_id"):
            c = crime()
            c.ID = request.POST.get("ID")
            #c.Date = request.POST.get("Date")
            c.Type = request.POST.get("Type")
            #c.Arrest = request.POST.get("Arrest")
            c.Area_id = request.POST.get("Area_id")
            c.save()
            return render(request, 'crime_app/insert_crime.html',{'c':c})
    return render(request,'crime_app/insert_crime.html',{'incomplete':"You must enter all the info to insert"})

def search_crime(request):
    if request.method=='GET':
        c_id = request.GET.get("ID")
        if c_id is not None:
            try:
                c = crime.objects.get(pk=c_id)
            except crime.DoesNotExist:
                return render(request,'crime_app/search_crime.html',{'dne':"Crime ID does not exist"})
            return render(request, 'crime_app/search_crime.html',{'c':c})

    return render(request, 'crime_app/search_crime.html')

def update_crime(request):
    if request.method=='POST':
        c_id = request.POST.get("ID")

        if c_id is not None:
            c = crime.objects.get(pk=c_id)
            if request.POST.get("Type"):
                c.Type = request.POST.get("Type")
            if request.POST.get("Area_id"):
                c.Area_id = request.POST.get("Area_id")

            c.save()
            return render(request, 'crime_app/update_crime.html',{'c':c})
    return render(request, 'crime_app/update_crime.html')


def delete_crime(request):
        if request.method=='POST':
            c_id = request.POST.get("ID")
            if c_id is not None:
                crime.objects.filter(pk=c_id).delete()
                return render(request, 'crime_app/delete_crime.html',{'c_id':c_id})

        return render(request, 'crime_app/delete_crime.html')



def main_page(request):
    return render(request,'crime_app/main.html')
