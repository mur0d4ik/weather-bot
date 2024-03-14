from aiogram import Router, F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message, CallbackQuery
from base import database
from keyboards import inline
from handlers.utils import words

router = Router()
db = database.DataBase()

db.cretae_table()

@router.message(CommandStart)
async def startCMD(message: Message):
    
    user_in_base = db.select_user(message.from_user.id)
    
    if user_in_base is None:
        await message.answer('🔽🔽🔽', reply_markup=inline.lang_generate().as_markup())
        
    else:
        await message.answer(f"{words[user_in_base[-1]]['try']} @{message.from_user.username}", reply_markup=inline.change_lang(user_in_base[-1]).as_markup())