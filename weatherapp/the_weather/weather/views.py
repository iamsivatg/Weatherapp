import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=14872417a93264239007d6b8b59fed02'
   
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()


    form = CityForm()

    cities = City.objects.all()

    data = []

    for city in cities:

        r = requests.get(url.format(city)).json()
        
        w = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
                }
    
        data.append(w)


    return render(request, 'weather/weather.html', context = {'data':data, 'form':form})
