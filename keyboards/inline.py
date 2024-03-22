import datetime

from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.utils import *
from aiogram.types import *
from translate import Translator
from base.database import DataBase

translator = Translator
db = DataBase()

def get_all_days_in_year():
    
    builder = InlineKeyboardBuilder()
    
    year = datetime.date.today().year
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    
    all_days = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]
        
    return builder
    
def change_lang(start: int, end: int, id: int):
    
    builder = InlineKeyboardBuilder()
    
    [builder.button(text=emoji[-1], callback_data=emoji[0]) for emoji in country_list[start: end]]
        
    if start == 9:
        builder.button(text='<', callback_data='<')
        
    else:
        builder.button(text='>', callback_data='>')
    
    builder.button(text=f"{translator(to_lang=db.select_user(id)[-1]).translate(text='Search')}🔎", callback_data='search')
    
    builder.adjust(3)
    
    return builder