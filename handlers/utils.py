from parsing import parser

words = {
    'ru': {
        'uni-code': '🇷🇺',
        'start': 'Привет ',
        'weather': parser.parsind_weather_func()
    },

    'en': {
        'uni-code': '🇺🇸',
        'start': 'Hi ',
        'weather': parser.parsind_weather_func()
    },

    'uz': {
        'uni-code': '🇺🇿',
        'start': 'Salom ',
        'weather': parser.parsind_weather_func()
    }
}