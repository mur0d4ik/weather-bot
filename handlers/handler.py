from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters.command import CommandObject, CommandStart, Command
from aiogram.fsm.context import FSMContext
from .utils import langs, words
from base.database import Users, UserSettings
from keyboards.inline import langs_keyboard, weather_type, settings_keyboard_current, settings_keyboard_forecast, back_a, back_b, switch_keyboard, switchs, repeat_request, days_kb, main_settings_keyboard
from keyboards.reply import get_location
from state.state import weatherStateCurrent, weatherStateForecast
from weather.weather import Weather

router = Router()
users_db = Users()
users_settings = UserSettings()

@router.message(CommandStart())
async def start_cmd(message: Message):

    if users_db.search_user(message.chat.id):
        await message.answer(f"{words[users_db.search_user(message.chat.id)[1]]['start']} @{message.from_user.username}")

    else:
        await message.answer(f"{words['en']['start']} @{message.from_user.username}")
        users_db.add_user(message.chat.id)
        users_settings.add_user_current(message.chat.id)
        users_settings.add_user_forecast(message.chat.id)

@router.message(Command(commands=['lang']))
async def lang_cmd(message: Message):
    await message.answer(words[users_db.search_user(message.chat.id)[1]]['lang'],
                        reply_markup=langs_keyboard(users_db.search_user(message.chat.id)[1]).as_markup())
    
@router.message(Command(commands=['weather']))
async def weather_cmd(message: Message):
    await message.answer(words[users_db.search_user(message.chat.id)[1]]['weather-cmd'],
                        reply_markup=weather_type(users_db.search_user(message.chat.id)[1]).as_markup())
    
@router.message(Command(commands=['settings']))
async def settings_cmd(message: Message):
    await message.answer(words[users_db.search_user(message.chat.id)[1]]['settings'],
                        reply_markup=main_settings_keyboard().as_markup())

@router.message(weatherStateCurrent.location)
async def weather_state(message: Message, state: FSMContext):

    await message.answer(words[users_db.search_user(message.chat.id)[1]]['please-second'], 
                                reply_markup=ReplyKeyboardRemove())

    await message.delete()

    if message.location:
        await message.answer(Weather().current_weather(message.chat.id, users_db.search_user(message.chat.id)[1],
                            [message.location.latitude, message.location.longitude]),
                            reply_markup=repeat_request().as_markup())
        
        await state.clear()

    else:
        await message.answer(words[users_db.search_user(message.chat.id)[1]]['location-eror-text'])

@router.message(weatherStateForecast.location)
async def weather_state(message: Message, state: FSMContext):
    
    await message.answer(words[users_db.search_user(message.chat.id)[1]]['please-second'], 
                                reply_markup=ReplyKeyboardRemove())

    await message.delete()

    data = await state.get_data()
    
    if message.location:
        await message.answer(Weather().forecast_weather(int(data.get('day')), message.chat.id,
                            users_db.search_user(message.chat.id)[1], [message.location.latitude, message.location.longitude]))
        
        await state.clear()

    else:
        await message.answer(words[users_db.search_user(message.chat.id)[1]]['location-eror-text'])

@router.callback_query()
async def any_callback(call: CallbackQuery, state: FSMContext):
    
    if call.data in langs:
        users_db.update_lang(call.message.chat.id, call.data)
        await call.message.edit_text(words[users_db.search_user(call.message.chat.id)[1]]
                                    [users_db.check_update_lang(call.message.chat.id, call.data)])
        
    elif call.data in ['current', 'forecast']:
       
        if call.data == 'current':
            await state.set_state(weatherStateCurrent.location)

        else:
            await call.message.edit_text(words[users_db.search_user(call.message.chat.id)[1]]['day'],
                                      reply_markup=days_kb().as_markup())

    elif call.data in back_a.values() and call.data not in back_b.values():
        await call.message.edit_text(text=call.data,
                                    reply_markup=switch_keyboard(users_settings.search_user_param(call.message.chat.id, call.data)).as_markup())

    elif call.data in back_b.values():
        await call.message.edit_text(text=call.data,
                                    reply_markup=switch_keyboard(users_settings.search_user_param(call.message.chat.id, call.data, 'forecast')).as_markup())

    elif call.data in ['current_settings', 'forecast_settings']:
        if call.data == 'current_settings':
            await call.message.edit_text(words[users_db.search_user(call.message.chat.id)[1]]['settings'],
                        reply_markup=settings_keyboard_current().as_markup())
            
        else:
            await call.message.edit_text(words[users_db.search_user(call.message.chat.id)[1]]['settings'],
                        reply_markup=settings_keyboard_forecast().as_markup())

    elif call.data in switchs:

        users_db.update_settings(call.message.chat.id)
        
        if call.message.text in back_a.values() and call.message.text not in back_b.values():
            users_settings.update_settings(call.message.chat.id, call.message.text, call.data)

            result_func = users_settings.check_update_lang(call.message.chat.id, call.message.text, call.data)


        elif call.message.text in back_b.values() and call.message.text not in back_a.values():
            users_settings.update_settings(call.message.chat.id, call.message.text, call.data, 'forecast')

            result_func = users_settings.check_update_lang(call.message.chat.id, call.message.text, call.data, 'forecast')

            
        else:
            users_settings.update_settings(call.message.chat.id, call.message.text, call.data)
            users_settings.update_settings(call.message.chat.id, call.message.text, call.data, 'forecast')

            result_func = users_settings.check_update_lang(call.message.chat.id, call.message.text, call.data)

        if len(result_func) == 1:
            await call.message.edit_reply_markup(reply_markup=switch_keyboard(call.data).as_markup())

        else:
            await call.message.edit_text(words[users_db.search_user(call.message.chat.id)[1]][result_func])

    elif call.data == 'back_param':
        await call.message.edit_text(words[users_db.search_user(call.message.chat.id)[1]]['settings'],
                        reply_markup=main_settings_keyboard().as_markup())
        
    elif call.data == 'repeat_request_current':
        await call.message.answer(words[users_db.search_user(call.message.chat.id)[1]]['weather-state'],
                                    reply_markup=get_location(users_db.search_user(call.message.chat.id)[1]).as_markup(resize_keyboard=True))
        
        await state.set_state(weatherStateCurrent.location)

    elif int(call.data) in range(1, 31):
        await call.message.answer(words[users_db.search_user(call.message.chat.id)[1]]['weather-state'],
                                  reply_markup=get_location(users_db.search_user(call.message.chat.id)[1]).as_markup(resize_keyboard=True))

        await state.update_data(day = call.data)

        await state.set_state(weatherStateForecast.location)