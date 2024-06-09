from base.database import UserSettings

def beautiful_text_current(id: int, lang:str, data: dict[str|list]):
    words_langs = {
        'ru': {
            'lat_lon': f'Широта и долгота: ',
            'last_updated': f'Время последного обновление данных: ',
            'temp_c': f'Температура в °C | ',
            'temp_f': f'Температура в °F | ',
            'condition': f'Погода: ',
            'humidity': 'Влажность: '
        },

        'en': {
            'lat_lon': f'Latitude and longitude: ',
            'last_updated': f'Time of last data update: ',
            'temp_c': f'Temperature in °C | ',
            'temp_f': f'Temperature in °F | ',
            'condition': f'Weather: ',
            'humidity': 'Humidity: '
        },

        'uz': {
            'lat_lon': f'Kenglik va uzunlik: ',
            'last_updated': f'Ma\'lumotlarning oxirgi yangilanish vaqti: ',
            'temp_c': f'Harorat °C | ',
            'temp_f': f'Harorat °F | ',
            'condition': f'Ob-havo: ',
            'humidity': 'Namlik: '
        },

        'ar': {
            'lat_lon': f'خطوط الطول والعرض: ',
            'last_updated': f'وقت آخر تحديث للبيانات: ',
            'temp_c': f'درجة الحرارة في °C | ',
            'temp_f': f'درجة الحرارة في °F | ',
            'condition': f'طقس: ',
            'humidity': 'رطوبة: '
        },

        'uk': {
            'lat_lon': f'Широта і довгота: ',
            'last_updated': f'Час останнього оновлення даних: ',
            'temp_c': f'Температура в °C | ',
            'temp_f': f'Температура в °F | ',
            'condition': f'Погода: ',
            'humidity': 'Вологість: '
        }
    }

    params = ['lat_lon', 'last_updated', 'temp_c', 'temp_f', 'condition', 'humidity']
    
    result_text = ''
    
    user_data = UserSettings().search_user(id)[1:]

    for i in range(len(user_data)):
        if user_data[i] != '❌':
            result_text += f"{words_langs[lang][params[i]]}{data[params[i]]}\n\n"

    return result_text



def beautiful_text_forecast(id: int, lang:str, data: dict[str|list]):
    words_langs = {
        'ru': {
            'lat_lon': 'Широта и долгота: ',
            'sunrise': 'Восход: ',
            'sunset': 'Закат: ',
            'moonrise': 'Восход луны: ',
            'moonset': 'Закат луны: ',
            'max_min_temp_c': 'МАКС-МИН температура в °C | ',
            'max_min_temp_f': 'МАКС-МИН температура в °F | ',
            'condition': 'Cостояние: ',
            'humidity': 'Влажность: ',
            'wind_kph': 'Ветер км/ч: ',
            'wind_mph': 'Ветер миль/ч: '
        },

        'en': {
            'lat_lon': 'Latitude and longitude: ',
            'sunrise': 'Sunrise: ',
            'sunset': 'Sunset: ',
            'moonrise': 'Moonrise: ',
            'moonset': 'Moonset: ',
            'max_min_temp_c': 'MAX-MIN temperature in °C | ',
            'max_min_temp_f': 'MAX-MIN temperature in °F | ',
            'condition': 'Condition: ',
            'humidity': 'Humidity: ',
            'wind_kph': 'Wind| kph: ',
            'wind_mph': 'Wind| mph: '
        },

        'uz': {
            'lat_lon': 'Kenglik va uzunlik: ',
            'sunrise': 'Quyosh chiqishi: ',
            'sunset': 'Quyosh botishi: ',
            'moonrise': 'Oy chiqishi: ',
            'moonset': 'Oy botishi: ',
            'max_min_temp_c': 'MAX-MIN harorat °C | ',
            'max_min_temp_f': 'MAX-MIN harorat °F | ',
            'condition': 'Ob-havo: ',
            'humidity': 'Namlik: ',
            'wind_kph': 'Shamol| kph: ',
            'wind_mph': 'Shamol| mph: '
        },

        'ar': {
            'lat_lon': 'خطوط الطول والعرض: ',
            'sunrise': 'شروق الشمس: ',
            'sunset': 'غروب: ',
            'moonrise': 'طلوع القمر: ',
            'moonset': 'غروب الشمس: ',
            'max_min_temp_c': 'درجة الحرارة القصوى والدقيقة في °C |',
            'max_min_temp_f': 'درجة الحرارة القصوى والدقيقة في °F |',
            'condition': 'حالة: ',
            'humidity': 'رطوبة: ',
            'wind_kph': 'الريح| kph:',
            'wind_mph': 'الريح| mph'
        },

        'uk': {
            'lat_lon': 'Широта і довгота: ',
            'sunrise': 'Схід сонця: ',
            'sunset': 'Захід сонця: ',
            'moonrise': 'Cхід місяця',
            'moonset': 'Захід місяця',
            'max_min_temp_c': 'MAX-MIN температура в °C |',
            'max_min_temp_f': 'MAX-MIN температура в °F |',
            'condition': 'Хвороба: ',
            'humidity': 'Вологість: ',
            'wind_kph': 'Вітер| kph: ',
            'wind_mph': 'Вітер| mph: '
        }
    }

    params = ['lat_lon', 'sunrise', 'sunset', 'moonrise', 'moonset', 'max_min_temp_c', 'max_min_temp_f', 'condition', 'humidity', 'wind_kph', 'wind_mph']
    
    result_text = ''
    
    user_data = UserSettings().search_user(id, 'forecast')[1:]

    for i in range(len(user_data)):
        if user_data[i] != '❌':
            result_text += f"{words_langs[lang][params[i]]}{data[params[i]]}\n\n"

    return result_text
