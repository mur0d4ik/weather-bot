import os
import requests
import datetime

from dotenv import load_dotenv
from opencage.geocoder import OpenCageGeocode
from base.database import DataBase
from . import utils


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'config.env'))

class Weather():
    
    def __init__(self) -> None:
        self.api = os.getenv("weatherAPI")
        self.geo_name_api = os.getenv("geo_nameAPI")

    def real_time(self, user_id: int, lang: str, city: str = 'London', location: list[float|float] = []):
        """
        Это функция вернет прогноз погоды на текущий момент!
        """
        
        
        if location == []:
            response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={self.api}&lang={lang}&q={city}")

        else:
            city = OpenCageGeocode(self.geo_name_api).reverse_geocode(location[0], location[-1])[0]['formatted']
            response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={self.api}&lang={lang}&q={location[0]},{location[-1]}")
        
        if response.status_code != 200:
            return utils.eror_text[DataBase().select_user(user_id)[-1]]['location-eror']
        
        return utils.weather_lang(city,
        response.json()['current']['last_updated'],
        response.json()['current']['wind_mph'],
        response.json()['current']['wind_kph'],
        response.json()['current']['temp_c'],
        response.json()['current']['temp_f'],
        response.json()['current']['condition']['text'],
        lang)
        
    def forecast(self, user_id: int, lang: str, day: str, city: str = 'London', location: list[float|float] = []):
        if location == []:
            response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={self.api}&lang={lang}&q={city}&days={day}")

        else:
            city = OpenCageGeocode(self.geo_name_api).reverse_geocode(location[0], location[-1])[0]['formatted']
            response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={self.api}&lang={lang}&q={location[0]},{location[-1]}&days={day}")

        if response.status_code != 200:
            return utils.eror_text[DataBase().select_user(user_id)[-1]]['location-eror']
        
        for i in response.json()['forecast']['forecastday']:
            if i['date'][-2:] == day and i['date'][-5: -3].replace('0', '') == str(datetime.datetime.now().month):
                
                return utils.weather_forecast(city,
                i['date'],
                i['day']['maxwind_mph'],
                i['day']['maxwind_kph'],
                i['day']['mintemp_c'],
                i['day']['maxtemp_c'],
                i['day']['mintemp_f'],
                i['day']['maxtemp_c'],
                i['day']['condition']['text'],
                lang)
                    