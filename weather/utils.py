

def weather_lang(location: str, last_update: str, wind_mph: int|float, wind_kph: int|float, temperature_c: int|float, temperature_f: int|float, day_text: str, lang: str):

    langs = {
        'ru': f"""Ваше местоположения: <tg-spoiler>{location}</tg-spoiler>

⏰  Последнее обновление: {last_update}

🌡
Текущая температура в градусах цельсия: {temperature_c}°C
Текущая температура в градусах фаренгейта: {temperature_f}°F

⛅️  Погодное условия: {day_text}

💨
Скорость ветра в миль/час: {wind_mph}
Скорость ветра в км/час: {wind_kph}
""",
        'en': f"""Your location: <tg-spoiler>{location}</tg-spoiler>

⏰  Last update: {last_update}

🌡
Current temperature in degrees Celsius: {temperature_c}°C
Current temperature in degrees Fahrenheit: {temperature_f}°F

⛅️  Weather conditions: {day_text}

💨
Wind speed in mph: {wind_mph}
Wind speed in km/h: {wind_kph}
""",

        'uz': f"""Joylashuvingiz: <tg-spoiler>{location}</tg-spoiler>

⏰  Oxirgi yangilanish: {last_update}

🌡
Tselsiy bo'yicha joriy harorat: {temperature_c}°C
Joriy harorat Farengeyt darajasida: {temperature_f}°F

⛅️  Ob-havo sharoiti: {day_text}

💨
Shamol tezligi mil/soat: {wind_mph}
Shamol tezligi km/soat: {wind_kph}
"""
    }


    return langs[lang]

def weather_forecast(location: str, date: str, max_wind_mph: int|float, max_wind_kph: int|float, min_temperature_c: int|float, max_temperature_c: int|float, min_temperature_f: int|float, max_temperature_f: int|float, day_text: str, lang: str):
    langs = {
        'ru': f"""Ваше местоположения: <tg-spoiler>{location}</tg-spoiler>

🗓  {date}

🌡
Температура в градусах цельсия: {min_temperature_c} - {max_temperature_c}°C
Температура в градусах фаренгейта: {min_temperature_f} - {max_temperature_f}°F

⛅️  Погодное условия: {day_text}

💨
Скорость ветра в миль/час: {max_wind_mph} 
Скорость ветра в км/час: {max_wind_kph}
""",

        'en': f"""Your location: <tg-spoiler>{location}</tg-spoiler>

🗓  {date}

🌡
Current temperature in degrees Celsius: {min_temperature_c} - {max_temperature_c}°C
Current temperature in degrees Fahrenheit: {min_temperature_f} - {max_temperature_f}°F

⛅️  Weather conditions: {day_text}

💨
Wind speed in mph: {max_wind_mph}
Wind speed in km/h: {max_wind_kph}
""",
        
        'uz': f"""Joylashuvingiz: <tg-spoiler>{location}</tg-spoiler>

🗓  {date}

🌡
Tselsiy bo'yicha joriy harorat: {min_temperature_c} - {max_temperature_c}°C
Joriy harorat Farengeyt darajasida: {min_temperature_f} - {max_temperature_f}°F

⛅️  Ob-havo sharoiti: {day_text}

💨
Shamol tezligi mil/soat: {max_wind_mph}
Shamol tezligi km/soat: {max_wind_kph}
"""
    }

    return langs[lang]


eror_text = {
    'ru': {
        'location-eror': 'Вы не правильно ввели!'
    },

    'en': {
        'location-eror': 'You entered it incorrectly!'
    },

    'uz': {
        'location-eror': "Siz uni noto'g'ri kiritdingiz!"
    }
}