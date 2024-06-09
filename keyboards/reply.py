from aiogram.utils.keyboard import ReplyKeyboardBuilder
from handlers.utils import words

def get_location(lang: str):

    builder = ReplyKeyboardBuilder()

    builder.button(text=words[lang]['get-location'], request_location=True)

    return builder