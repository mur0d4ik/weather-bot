import os
import requests
import datetime

from dotenv import load_dotenv
from opencage.geocoder import OpenCageGeocode
from .utils import beautiful_text_current, beautiful_text_forecast

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'config.env'))

class Weather():
    
    def __init__(self) -> None:
        self.api = os.getenv("weatherAPI")
        self.geo_name_api = os.getenv("geo_nameAPI")

    def current_weather(self, id: int, lang: str, location: list[float]) -> dict[str, str | list[str | int]] | str:
        url = f"https://api.weatherapi.com/v1/current.json?key={self.api}&lang={lang}&q={location[0]},{location[1]}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            result_date = {
                'lat_lon': f"{data['location']['lat']} {data['location']['lon']}",
                'last_updated': data['current']['last_updated'][data['current']['last_updated'].index(' '):],
                'temp_c': data['current']['temp_c'],
                'temp_f': data['current']['temp_f'],
                'condition': data['current']['condition']['text'],
                'humidity': data['current']['humidity']
            }

            return beautiful_text_current(id, lang, result_date)

        else:
            return 'eror-lang'
        
    def forecast_weather(self, day: int, id: int, lang: str, location: list[float]) -> dict[str, str | list[str | int]] | str:
        url = f"https://api.weatherapi.com/v1/forecast.json?key={self.api}&lang={lang}&q={location[0]},{location[1]}&days=3"

        response = requests.get(url)

        result_date = {}

        if response.status_code == 200:
            data = response.json()

            for i in data['forecast']['forecastday']:
                if day == int(i['date'][-2:]):
                    result_date = {
                        'lat_lon': f"{data['location']['lat']},{data['location']['lon']}| {data['location']['tz_id']}",
                        'sunrise': f"{data['forecast']['forecastday'][1]['astro']['sunrise']}",
                        'sunset': f"{data['forecast']['forecastday'][1]['astro']['sunset']}",
                        'moonrise': f"{data['forecast']['forecastday'][1]['astro']['moonrise']}",
                        'moonset': f"{data['forecast']['forecastday'][1]['astro']['moonset']}",
                        ####################
                        'max_min_temp_c': f"{data['forecast']['forecastday'][0]['day']['mintemp_c']} - {data['forecast']['forecastday'][0]['day']['maxtemp_c']}",
                        'max_min_temp_f': f"{data['forecast']['forecastday'][0]['day']['mintemp_f']} - {data['forecast']['forecastday'][0]['day']['maxtemp_f']}",
                        'condition': f"{data['forecast']['forecastday'][0]['day']['condition']['text']}",
                        'humidity': f"{data['current']['humidity']}",
                        'wind_kph': f"{data['current']['wind_kph']}",
                        'wind_mph': f"{data['current']['wind_mph']}"
                    }
                    
                    return beautiful_text_forecast(id, lang, result_date)

        else:
            return 'eror-lang'