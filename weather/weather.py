import requests
import os

def weather_func():
    api = '6a6ec55a58284d75851161941241403'

    url = f'http://api.weatherapi.com/v1/forecast.json?key={api}&q=Tashkent&days=7'

    response = requests.get(url)
    
    print(response.json()['forecast']['forecastday'])
    
# weather_func()