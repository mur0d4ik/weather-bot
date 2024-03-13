from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.utils import words

def lang_generate():

    builder = InlineKeyboardBuilder()

    for key, value in words.items():
        builder.button(text = value['uni-code'], callback_data = key)

    return builder