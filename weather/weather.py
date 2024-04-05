import os
import requests

from dotenv import load_dotenv
from opencage.geocoder import OpenCageGeocode
from base.database import DataBase
from . import utils


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'config.env'))

class Weather():
    
    def __init__(self) -> None:
        self.api = os.getenv("weatherAPI")
        self.geo_name_api = os.getenv("geo_nameAPI")

    def real_time(self, lang: str, city: str = 'London', location: list[float|float] = []):
        if location == []:
            location_name = city
            response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={self.api}&lang={lang}&q={city}")

        else:
            location_name = OpenCageGeocode(self.geo_name_api).reverse_geocode(location[0], location[-1])[0]['formatted']
            response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={self.api}&lang={lang}&q={location[0]},{location[-1]}")

        return utils.weather_lang(location_name,
        response.json()['current']['last_updated'],
        response.json()['current']['wind_mph'],
        response.json()['current']['wind_kph'],
        response.json()['current']['temp_c'],
        response.json()['current']['temp_f'],
        response.json()['current']['condition']['text'],
        lang
        )