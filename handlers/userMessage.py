from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from .utils import words
from base.database import DataBase

router = Router()
db = DataBase()

@router.callback_query()
async def lang(call: CallbackQuery):
    user_in_base = db.select_user(call.message.chat.id)
    
    if user_in_base is None and call.data in words[call.data]:
        await call.message.answer(f"{words[call.data]['start']} @{call.message.chat.username}!")
        db.add_user(call.message.chat.id, call.data)