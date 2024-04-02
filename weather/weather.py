import requests
import os

from dotenv import load_dotenv
import reverse_geocoder as rs

load_dotenv(dotenv_path='config.env')

def get_location(lat, lon):    
    location = rs.search((lat, lon))
    
    return location[0]['name']


class Weather():
    
    def __init__(self) -> None:
        self.api = os.getenv("API")
        self.api_geo_name = os.getenv("API_GEO_NAME")
           
    def real_time(self, city: str, location: list[float, float] = []):
        
        if location == []:
            url = f'http://api.weatherapi.com/v1/current.json?key={self.api}&q={city}'
        
        else:
            url = f'http://api.weatherapi.com/v1/current.json?key={self.api}&q={location[0]},{location[-1]}'
            url_geo_name = f'https://api.opencagedata.com/geocode/v1/json?q={location[-1]}%2C{location[0]}&key={self.api_geo_name}'
            
            geo_name = requests.get(url_geo_name)
        
        response = requests.get(url)
        
        return  f"""📍 Location: {geo_name.json()['results'][0]['components']['county']}, {geo_name.json()['results'][0]['components']['neighbourhood']}, {geo_name.json()['results'][0]['components']['house_number']}

    -   latitude: <code>{response.json()['location']['lat']}</code>
    -   longitude: <code>{response.json()['location']['lon']}</code>

⏲️ Date|Time: {response.json()['location']['localtime']}

🗓 Day: {response.json()['current']['condition']['text']}

🌡 Temp. {response.json()['current']['temp_c']}°C
🌡 Temp. {response.json()['current']['temp_f']}°F

💨 Wind speed: {response.json()['current']['wind_mph']}mph
💨 Wind speed: {response.json()['current']['wind_kph']}kph

"""

    def clockwise(self, city: str, time: str, location: list[float, float] = []):
        
        if location == []:
            url = f'http://api.weatherapi.com/v1/forecast.json?key={self.api}&q={city}&days=1'
        
        else:
            url = f'http://api.weatherapi.com/v1/forecast.json?key={self.api}&q={location[-1]},{location[0]}&days=1'
            url_geo_name = f'https://api.opencagedata.com/geocode/v1/json?q={location[-1]}%2C{location[0]}&key={self.api_geo_name}'
            geo_name = requests.get(url_geo_name)
            
        response = requests.get(url)

        for _ in response.json()['forecast']['forecastday'][0]['hour']:
            if time in _['time']:
                return  f"""📍 Location: <tg-spoiler>{geo_name.json()['results'][0]['components']['county']}, {geo_name.json()['results'][0]['components']['neighbourhood']}, {geo_name.json()['results'][0]['components']['house_number']}</tg-spoiler> 

    -   latitude: <code>{response.json()['location']['lat']}</code>
    -   longitude: <code>{response.json()['location']['lon']}</code>

⏲️ Date|Time: {response.json()['location']['localtime']}

🗓 Day: {response.json()['current']['condition']['text']}

🌡 Temp. {response.json()['current']['temp_c']}°C
🌡 Temp. {response.json()['current']['temp_f']}°F

💨 Wind speed: {response.json()['current']['wind_mph']}mph
💨 Wind speed: {response.json()['current']['wind_kph']}kph
"""