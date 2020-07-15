from django.shortcuts import render, redirect
import requests


def index(request):
        if request.method == 'POST':
                url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=458f3827e9cbd3d04baa56e53dc349fd'
                city = request.POST['city']
                city_weather = requests.get(url.format(city)).json()
          

                weather = {
                        'city' : city_weather['name'],
                        'temperature' : city_weather['main']['temp'],
                        'feels' : city_weather['main']['feels_like'],
                        'humidity' : city_weather['main']['humidity'],
                        'description' : city_weather['weather'][0]['description'],
                        'icon' : city_weather['weather'][0]['icon'],
                        'country' : city_weather['sys']['country']
                        }
        
                context = {'weather' : weather}
                return render(request, 'index.html', context)

               

        else:
                url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=458f3827e9cbd3d04baa56e53dc349fd'
                city = 'Cabuyao'
                city_weather = requests.get(url.format(city)).json()
                       
                weather = {
                        'city' : city_weather['name'],
                        'temperature' : city_weather['main']['temp'],
                        'feels' : city_weather['main']['feels_like'],
                        'humidity' : city_weather['main']['humidity'],
                        'description' : city_weather['weather'][0]['description'],
                        'icon' : city_weather['weather'][0]['icon'],
                        'country' : city_weather['sys']['country']
                        }

                context = {'weather' : weather}
 
                return render(request, 'index.html', context)


def about(request):
        return render(request, 'about.html', {})