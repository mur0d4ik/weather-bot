from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.utils import words

def lang_generate():

    builder = InlineKeyboardBuilder()

    for key, value in words.items():
        builder.button(text=value['uni-code'], callback_data=key)

    return builder

def change_lang(lang: str):
    
    builder = InlineKeyboardBuilder()
    
    for key, value in words[lang]['change_lang'].items():
        builder.button(text=key, callback_data=value)
        
    return builder
    
    