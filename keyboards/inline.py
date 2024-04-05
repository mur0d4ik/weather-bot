from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.utils import *

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

    function_dict = {
        'en': {
            'now': 'Current weather ⏰'
        },

        'ru': {
            'now': 'Текущую погоду ⏰'
        },

        'uz': {
            'now': 'Hozirgi ob-havoni ⏰'
        }
    }

    user_in_base = DataBase().select_user(user_id)

    for key, value in function_dict[user_in_base[-1]].items():
        builder.button(text=value, callback_data=key)
    
    return builder