from aiogram.types import BotCommand
from base.database import DataBase

def bot_commands():
    commands = {
        'ru': {
            '/start': 'Запустить бота! 🚀',
            '/lang': 'Изменить язык! 🌍',
            '/weather': 'Узнать погоду! ⛅️' 
            },

        'en': {
            '/start': 'Start the bot! 🚀',
            '/lang': 'Change language! 🌍',
            '/weather': 'Check the weather! ⛅️'
        },

        'uz': {
            '/start': 'Botni ishga tushiring! 🚀',
            '/lang': 'Tilni o\'zgartiring! 🌍',
            '/ob-havo': 'Ob-havoni tekshiring! ⛅️'
        }
    }

    result = []

    for cmd, description in commands['en'].items():
        result.append(BotCommand(command=cmd, description=description))
        
    return result
