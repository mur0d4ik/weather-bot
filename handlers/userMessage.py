import asyncio

from translate import Translator
from aiogram import Router, F
from aiogram.types import *
from base.database import DataBase
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from state.state import *

from .utils import *
from keyboards.inline import *

router = Router()
db = DataBase()
storage = MemoryStorage()
translator = Translator
        
@router.message(CommandStart())
async def commands(message: Message):
    db.add_user(message.chat.id, 'en')
    await message.answer(f"{translator(to_lang=db.select_user(message.chat.id)[-1]).translate(words['start'])} @{message.from_user.username}")

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
        await call.message.answer(translator(to_lang=db.select_user(call.message.chat.id)[-1]).translate(text=words[call.data]))
        
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
    
    await message.answer(f"⚠️ {translator(to_lang=db.select_user(message.chat.id)[-1]).translate(search_lang(message.chat.id, message.text))}")
    
    await state.clear()