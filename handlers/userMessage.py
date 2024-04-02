import asyncio

from translate import Translator
from aiogram import Router, F
from aiogram.types import *
from base.database import DataBase
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from state.state import *
from weather.weather import Weather


from .utils import *
from keyboards.inline import *
from keyboards.reply import *

router = Router()
db = DataBase()
storage = MemoryStorage()
translator = Translator
weathers = Weather()
        
@router.message(CommandStart())
async def commands(message: Message):
    db.add_user(message.chat.id, 'en')
    await message.answer(f"{translator(to_lang=db.select_user(message.chat.id)[-1]).translate(words['start'])} @{message.from_user.username}")

@router.message(Command(commands=['weather']))
async def CMD_weather(message: Message):
    await message.answer(f"{translator(to_lang=db.select_user(message.chat.id)[-1]).translate(words['weather'])}🔽", reply_markup=weather(message.chat.id).as_markup())

@router.message(Command(commands=['lang']))
async def CMD_lang(message: Message):
    await message.answer(f"{translator(to_lang=db.select_user(message.chat.id)[-1]).translate(words['lang'])}🔽", reply_markup=change_lang(0, 9, message.chat.id).as_markup())

@router.callback_query()
async def callBack(call: CallbackQuery, state: FSMContext):
    
    if call.data == '>':
        await call.message.edit_reply_markup(reply_markup=change_lang(9, 18, call.message.chat.id).as_markup())
        
    elif call.data == '<':
        await call.message.edit_reply_markup(reply_markup=change_lang(0, 9, call.message.chat.id).as_markup())
        
    elif call.data == 'search':
        await state.set_state(SearchLang.lang)
        await call.message.edit_text(translator(to_lang=db.select_user(call.message.chat.id)[-1]).translate(text=words[call.data]))
    
    elif call.data == 'real_time':
        await call.message.edit_text(translator(to_lang=db.select_user(call.message.chat.id)[-1]).translate(text=weathers.real_time('Tashkent')), parse_mode='HTML')
        
    elif call.data == 'clockwise' or call.data == '<<':
        await call.message.edit_text(f"{translator(to_lang=db.select_user(call.message.chat.id)[-1]).translate(text=words['clockwise'])} ⏰", reply_markup=clockwise_btn(0, 13).as_markup())
    
    elif call.data == '>>':
        await call.message.edit_reply_markup(f"{translator(to_lang=db.select_user(call.message.chat.id)[-1]).translate(text=words['clockwise'])} ⏰", reply_markup=clockwise_btn(13, 24).as_markup())
        
    elif call.data[-2:] == '00':
        global select_time
        select_time = call.data 
        
        await call.message.delete()
        await state.set_state(WeatherS.location)
        await call.message.answer(f"{translator(to_lang=db.select_user(call.message.chat.id)[-1]).translate(words['clockwise_state'])}", reply_markup=location_btn().as_markup(resize_keyboard=True), parse_mode='HTML')
    
    else:
        for country in country_list:
            if call.data == country[0]:
                changed_or_no = db.update_lang(call.message.chat.id, call.data)
                
                if changed_or_no is True:
                    await call.message.edit_text(f"{translator(to_lang=country[0]).translate(words['changed_lang'])}✅")
                    
                else:
                    await call.message.edit_text(f"{translator(to_lang=db.select_user(call.message.chat.id)[-1]).translate(words['changed_lang_eror'])}❌")
    
@router.message(SearchLang.lang)
async def searhc_lang(message: Message, state: FSMContext):
    
    await state.update_data(lang=message.text)
    
    text_succeful = search_lang(message.chat.id, message.text)
    
    await message.answer(f"⚠️ {translator(to_lang=db.select_user(message.chat.id)[-1]).translate(text_succeful)}")
    
    await state.clear()
    
@router.message(WeatherS.location)
async def select_lang(message: Message):
    
    if message.location:
        await message.answer(translator(to_lang=db.select_user(message.chat.id)[-1]).translate(text=weathers.clockwise('', select_time, [message.location.longitude, message.location.latitude])), reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')
        
    else:
        await message.answer(translator(to_lang=db.select_user(message.chat.id)[-1]).translate(text=weathers.clockwise(message.text, select_time)), reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')
