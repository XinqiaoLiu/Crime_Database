from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import district, crime, danger, district_id
from django.http import Http404
from django.contrib import messages
import datetime
from django.db.models import Count
from django.db import connection
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
        if request.POST.get("ID") and request.POST.get("Type") and request.POST.get("Area_id") and request.POST.get("Time"):
            c = crime()
            c.ID = request.POST.get("ID")
            c.Ctime = request.POST.get("Time")
            c.Type = request.POST.get("Type")
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
            if request.POST.get("Time"):
                c.Ctime = request.POST.get("Time")
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

def recommend(request):
    if request.method=='GET':
        g = request.GET.get("Gender")
        a = request.GET.get("Age")
        v = request.GET.get("Visit")


        if a is not None and a!='':
            a = int(a)
            age_group = GetAgeGroup(a)

            num_crime = 0
            with connection.cursor() as cursor:
                cursor.callproc("GetCrimeCount",[v,num_crime])
                cursor.execute('select @_GetCrimeCount_1')
                num_crime = cursor.fetchall()[0][0]
            v_id = district_id.objects.filter(Neighborhood=v).values('ID')[0]['ID']
            #num_crime = crime.objects.filter(Area_id=v_id).count()
            crime_query = crime.objects.filter(Area_id=v_id).values('Type').annotate(t_count=Count('Type')).order_by('-t_count')
            crime_list = []
            for item in crime_query:
                crime_list.append((item['t_count'],item['Type']))
            danger_level = 0.0
            for first,second in crime_list:

                danger_level += first*danger.objects.filter(Type = second,Gender = g, Age = age_group).values('Level')[0]['Level']

            danger_level /= num_crime
            danger_level*=1.3
            return render(request, 'crime_app/recommend.html',{'num_crime':num_crime,'crime_list':crime_list,'danger':danger_level})
    return render(request, 'crime_app/recommend.html')

def route(request):
    if request.method=='GET':
        g = request.GET.get("Gender")
        a = request.GET.get("Age")

        t = request.GET.get("Time")
        v1 = request.GET.get("Visit1")
        v2 = request.GET.get("Visit2")
        v3 = request.GET.get("Visit3")

        if a is not None and a!='':
            info = [g,a,t,v1,v2,v3]
            a = int(a)
            age_group = GetAgeGroup(a)
            date = t.split(" ")[0]
            time = t.split(" ")[1]
            month = date.split("-")[1]
            day = date.split("-")[2]
            hour = time.split(":")[0]
            minute = time.split(":")[1]
            print(hour)
            if 23-int(hour) <= 3:
                return render(request, 'crime_app/route.html',{'late':1,'time':time})
            interval = int((23-int(hour))/3)
            print(interval)
            v_list = [v1,v2,v3]
            rate_list_list = []
            rec_route = []
            rec_route_idx = []
            for v in v_list:
                rate_list = []
                for j in range(3):
                    shour = str(int(hour)+j*interval)
                    ehour = str(int(shour)+interval)

                    starttime = "2019-"+month+"-"+day+" "+shour+":00"
                    endtime = "2019-"+month+"-"+day+" "+ehour+":00"
                    rate = 0.0
                    print(v)
                    print(endtime)
                    with connection.cursor() as cursor:
                        print(cursor.callproc("GetDanger",[g,age_group,v,starttime,endtime,rate]))
                        cursor.execute('select @_GetDanger_5')
                        rate = cursor.fetchall()[0][0]
                        print(type(rate))

                    if rate==None:
                        rate = 0.1
                    print(rate)
                    rate_list.append(rate)
                rate_list_list.append(rate_list)
            min = float('inf')
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        if i==j or i==k or j==k:
                            continue;
                        if min>rate_list_list[0][i]+rate_list_list[1][j]+rate_list_list[2][k]:
                            min = rate_list_list[0][i]+rate_list_list[1][j]+rate_list_list[2][k]
                            rec_route_idx = [i,j,k]

            for i in range(3):
                for j in range(3):
                    if rec_route_idx[j] == i:
                        rec_route.append((v_list[j],str(int(hour)+i*interval)+":"+minute))
            f = True
            return render(request, 'crime_app/route.html',{'rec_route':rec_route,'info':info})
        else:
            return render(request, 'crime_app/route.html')
    return render(request, 'crime_app/route.html')
def main_page(request):
    return render(request,'crime_app/main.html')

def GetAgeGroup(a):
    age_group = "children"
    if a>14 and a<30:
        age_group = "adolescent"
    elif a>=30 and a<60:
        age_group = "adult"
    elif a>=60:
        age_group = "senior"
    return age_group
