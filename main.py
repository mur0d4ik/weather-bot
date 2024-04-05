import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import handler
from base.database import DataBase

load_dotenv(dotenv_path='config.env')

DataBase().create_table()

# Запуск бота
async def main():

    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()

    dp.include_routers(
        handler.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

print(f'Бот запустился!')

if __name__ == "__main__":
    asyncio.run(main())