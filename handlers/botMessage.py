from aiogram import Router, F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message, CallbackQuery
from base import database
from keyboards import inline

router = Router()
db = database.DataBase()

db.cretae_table()

@router.message(CommandStart)
async def startCMD(message: Message):
    await message.answer('🔽🔽🔽', reply_markup=inline.lang_generate().as_markup())