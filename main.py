import asyncio
import os

from aiogram import Bot, Dispatcher
from handlers import userMessage, botMessage
from dotenv import load_dotenv
from base import database

database.DataBase().cretae_table()

load_dotenv(dotenv_path='config.env')

# Запуск бота
async def main():
    global bot

    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()

    dp.include_routers(
        userMessage.router,
        botMessage.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

print(f'Бот запустился!')

if __name__ == "__main__":
    asyncio.run(main())