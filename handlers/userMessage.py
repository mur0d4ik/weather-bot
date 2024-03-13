from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from .utils import words
from base.database import DataBase

router = Router()
db = DataBase()

@router.callback_query()
async def lang(call: CallbackQuery):
    await call.message.answer(f"{words[call.data]['start']} @{call.message.from_user.username}!")