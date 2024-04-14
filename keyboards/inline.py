import datetime

from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.utils import *
from calendar import Calendar

from base.database import DataBase

def langsKeyboard(user_id: int):
    
    user_in_base = DataBase().select_user(user_id)

    builder = InlineKeyboardBuilder()

    if user_in_base is None:  
        for key, emoji in langs.items():
            builder.button(text=emoji, callback_data=key)

    else:
        for key, emoji in langs.items():
            
            if key == user_in_base[-1]:
                continue

            else:
                builder.button(text=emoji, callback_data=key)

    builder.adjust(2)

    return builder

def weatehrsKeyboard(user_id: int):

    builder = InlineKeyboardBuilder()

    global function_dict
    function_dict = {
        'en': {
            'now': 'Current weather ⏰',
            'forecast': 'Weather forecast 📊'
        },

        'ru': {
            'now': 'Текущую погоду ⏰',
            'forecast': 'Прогноз погоды 📊'
        },

        'uz': {
            'now': 'Hozirgi ob-havoni ⏰',
            'forecast': 'Ob-havo bashorati 📊'
        }
    }

    user_in_base = DataBase().select_user(user_id)

    for key, value in function_dict[user_in_base[-1]].items():
        builder.button(text=value, callback_data=key)
    
    return builder

def daysKeyboard():
    builder = InlineKeyboardBuilder()

    days = Calendar().itermonthdates(datetime.datetime.now().year, datetime.datetime.now().month)

    date = int(datetime.datetime.now().day)

    days_list = []

    [days_list.append(week.day) for week in days]

    for i in days_list[days_list.index(date): days_list.index(date) + 3]:
        builder.button(text=str(i), callback_data=str(i))

    builder.adjust(1)

    return builder

def repeatKeyboard(keys: str, lang: str):
    builder = InlineKeyboardBuilder()

    repeat_buttons = {
        'ru': '🔄 Повторить ещё раз!',
        'en': '🔄 Repeat again!',
        'uz': '🔄 Yana takrorlang!'
    }

    [builder.button(text = repeat_buttons[lang], callback_data = keys)]

    return builder

