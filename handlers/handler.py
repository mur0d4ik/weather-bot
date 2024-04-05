from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import CommandObject, CommandStart, Command
from aiogram.fsm.context import FSMContext
from keyboards.inline import *
from state.state import weatherState
from .utils import words
from weather.weather import Weather

router = Router()

@router.message(CommandStart())         # Обработка комманды "start"
async def start_cmd(message: Message):
    user_in_base = DataBase().select_user(message.chat.id)

    if user_in_base is None:
        await message.answer(f"{words['en']['start']} @{message.from_user.username}✋",
        reply_markup=langsKeyboard(message.chat.id).as_markup())

    else:
        await message.answer(f"{words[user_in_base[-1]]['weather']}")



@router.message(Command(commands=['weather']))      # Обработка комманды "weather"
async def weather_cmd(message: Message):
    await message.answer(words[DataBase().select_user(message.chat.id)[-1]]['weather-cmd'],
    reply_markup=weatehrsKeyboard(message.chat.id).as_markup())



@router.message(Command(commands=['lang']))         # Обработка комманды "lang"
async def lang_cmd(message: Message):
    await message.answer(f"{words[DataBase().select_user(message.chat.id)[-1]]['start']} @{message.from_user.username}✋",
    reply_markup=langsKeyboard(message.chat.id).as_markup())



@router.callback_query()
async def any_callbacks(call: CallbackQuery, state: FSMContext):

    if call.data in langs:
        DataBase().add_user(call.message.chat.id, call.data)
        await call.message.edit_text(words[call.data]['changed'])

    elif call.data == 'now':
        await call.message.edit_text(words[DataBase().select_user(call.message.chat.id)[-1]]['weather-state'])
        await state.set_state(weatherState.location)

    else:
        pass



@router.message(weatherState.location)
async def state_location(message: Message, state: FSMContext):
    
    if message.location:
        await message.answer(Weather().real_time(lang=DataBase().select_user(message.chat.id)[-1],
        location=[message.location.latitude, message.location.longitude]), parse_mode='HTML')

        await state.clear()

    elif message.text:
        await message.answer(Weather().real_time(lang=DataBase().select_user(message.chat.id)[-1],
        city=message.text), parse_mode='HTML')

        await state.clear()
    
    else:
        await message.answer(words[DataBase().select_user(message.chat.id)[-1]]['location-eror-text'])
