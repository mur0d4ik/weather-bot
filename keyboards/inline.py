import datetime

from translate import Translator
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.utils import *
from aiogram.types import *
from translate import Translator
from base.database import DataBase

translator = Translator
db = DataBase()
translator = Translator

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

def weather(id: int):
    
    builder = InlineKeyboardBuilder()
    
    weatehrs = {
        f"{translator(to_lang=db.select_user(id)[-1]).translate(text='Real Time')}": 'real_time',
        f"{translator(to_lang=db.select_user(id)[-1]).translate(text='Clockwise')}": 'clockwise'
    }
    
    [builder.button(text=key, callback_data=value) for key, value in weatehrs.items()]
    
    builder.adjust(1)
    
    return builder

def clockwise_btn(start: int, end: int):
    
    builder = InlineKeyboardBuilder()
    
    for i in range(start, end):
        if i < 9:
            builder.button(text=f'0{i}:00', callback_data=f'0{i}:00')
            
        else:
            builder.button(text=f'{i}:00', callback_data=f'{i}:00')
                
    if start < 10:
        builder.button(text='>', callback_data='>>')
        
    else:
        builder.button(text='<', callback_data='<<')        
        
    builder.adjust(3)
    
    return builder