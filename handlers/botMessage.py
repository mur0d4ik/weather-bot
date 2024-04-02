from translate import Translator
from aiogram import Router, F
from aiogram.types import Message
from base import database
from aiogram.filters import Command, CommandStart, CommandObject
from keyboards.inline import *
from .utils import words

router = Router()
db = database.DataBase()
translator = Translator

db.cretae_table()
