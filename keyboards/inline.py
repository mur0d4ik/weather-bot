import datetime

from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.utils import langs

def langs_keyboard(lang: str) -> InlineKeyboardBuilder:
    """
    lang - язык который выбирал юзер\n
    """
    builder = InlineKeyboardBuilder()

    [builder.button(text=value, callback_data=key) for key, value in langs.items() if key != lang]

    builder.adjust(2)

    return builder

def main_settings_keyboard() -> InlineKeyboardBuilder:
    
    builder = InlineKeyboardBuilder()

    [builder.button(text=key, callback_data=key) for key in ['current_settings', 'forecast_settings']]

    return builder

def settings_keyboard_current() -> InlineKeyboardBuilder:
    
    builder = InlineKeyboardBuilder()

    for key, value in back_a.items():
        builder.button(text=key, callback_data=value)

    builder.adjust(2)

    return builder

def settings_keyboard_forecast() -> InlineKeyboardBuilder:
    
    builder = InlineKeyboardBuilder()

    for key, value in back_b.items():
        builder.button(text=key, callback_data=value)

    builder.adjust(2)

    return builder

def switch_keyboard(answer: str) -> InlineKeyboardBuilder:

    builder = InlineKeyboardBuilder()

    builder.button(text=switchs[answer[0]], callback_data=switchs[answer[0]])
    builder.button(text='<<', callback_data='back_param')

    builder.adjust(1)

    return builder

def weather_type(lang: str) -> InlineKeyboardBuilder:

    builder = InlineKeyboardBuilder()

    weathers_type = {
        'ru': {
            'Сейчас': 'current',
            'Прогноз': 'forecast'
        },

        'en': {
            'Current': 'current',
            'Forecast': 'forecast'
        }, 

        'uz': {
            'Joriy': 'current',
            'Prognoz': 'forecast'
        },

        'ar': {
            'حاضِر': 'current',
            'تنبؤ بالمناخ': 'forecast'
        },

        'uk': {
            'Поточний': 'current',
            'Прогноз': 'forecast'
        }
    }

    [builder.button(text=key, callback_data=value) for key, value in weathers_type[lang].items()]

    return builder

def repeat_request() -> InlineKeyboardBuilder:

    builder = InlineKeyboardBuilder()

    builder.button(text='🔄', callback_data='repeat_request_current')

    return builder


def days_kb() -> InlineKeyboardBuilder:
    
    builder = InlineKeyboardBuilder()

    threeday = [(datetime.date.today() + datetime.timedelta(days=i)).day for i in range(1, 3)]

    [builder.button(text=str(i), callback_data=str(i)) for i in threeday]

    builder.adjust(1)

    return builder

back_a = {
        'lat - lon': 'lat_lon',
        'last_updated': 'last_updated',
        'temp_c': 'temp_c',
        'temp_f': 'temp_f',
        'condition': 'condition',
        'humidity': 'humidity'
    }

back_b = {
    'lat - lon': 'lat_lon',
    'sunrise': 'sunrise',
    'sunset': 'sunset',
    'moonrise': 'moonrise',
    'moonset': 'moonset',
    'max_min_temp_c': 'max_min_temp_c',
    'max_min_temp_f': 'max_min_temp_f',
    'condition': 'condition',
    'humidity': 'humidity',
    'wind_kph': 'wind_kph',
    'wind_mph': 'wind_mph'
}

switchs = {
        '✅': '❌',
        '❌': '✅'
    }