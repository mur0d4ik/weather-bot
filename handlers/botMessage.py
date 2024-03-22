from aiogram import Router, F
from aiogram.types import Message
from base import database
from .utils import words
from keyboards.inline import change_lang

router = Router()
db = database.DataBase()

db.cretae_table()
