from django.shortcuts import render
import urllib.request
import json
import math


# Create your views here.

def home(request):
    
    if request.method == 'POST':
        city = request.POST['city']

        
        data_source_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=63663f503c6adbbe0b8eb22748835e00').read()
        

        json_data = json.loads(data_source_url)

        weather = {
                'city' :city,
                'temperature' : math.ceil(json_data['main']['temp']-273.15),
                'description' : str(json_data['weather'][0]['description']),
                'icon' : json_data['weather'][0]['icon'],
                'country': str(json_data['sys']['country']),
                'humidity': json_data['main']['humidity'],
                'speed': json_data['wind']['speed'],
            }
        
    else:
        weather={}   

    
     
        
    return render(request,'home.html',weather)

