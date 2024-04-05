

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