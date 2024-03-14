from parsing import parser

words = {
    'ru': {
        'uni-code': '🇷🇺',
        'start': 'Привет ',
        'try' : 'Привет снова ',
        'lang': 'Хотите поменять язык?',
        'weather': parser.parsind_weather_func(),
        'change_lang': 
            {
                'Да ✅': 'yes',
                'Нет ❌': 'no'
            }
    },

    'en': {
        'uni-code': '🇺🇸',
        'start': 'Hi ',
        'try': 'Hi again ',
        'lang': 'Do you want to change the language?',
        'weather': parser.parsind_weather_func(),
        'change_lang':
        {
            'Yes ✅': 'yes',
            'No ❌': 'no'
        }
    },

    'uz': {
        'uni-code': '🇺🇿',
        'start': 'Salom ',
        'try': 'Yana bir marotaba salom ',
        'lang': "Tilni o'zgartirmoqchimsiz?",
        'weather': parser.parsind_weather_func(),
        'change_lang': 
        {
            'Xa ✅': 'yes',
            "Yo'q ❌": 'no'
        }
    }
}

