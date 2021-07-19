
from django.http import request
from django.shortcuts import render
import json
import urllib.request
from django.contrib import messages

# Create your views here.
def showdata(request):
    if request.method=='POST':
        city=request.POST['city']
        try:
             sourse=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=a2194a007b2f29c8641e88a6d5f0b732')
                                     
        except:
                data={}
                messages.warning(request,"City is not in our list")
                return render(request,'show.html',{'data':data})
                 
        converted=json.load(sourse)   
        if city==converted['name']and city!=None:
         data={
              "country":str(converted['sys']['country']),
              "city":str(converted['name']),
              "temprature":str(converted['main']['temp'])+'°C',
              "pressure":str(converted['main'][ 'pressure']),
              "humidity":str(converted['main'][ 'humidity']),
              "description":str(converted['weather'][0]['description']),
              'icon': converted['weather'][0]['icon'],
             }
       
        else:
           messages.warning(request,"City is not in our list")
           data={}


    else:
        data={}
    return render(request,'show.html',{'data':data})