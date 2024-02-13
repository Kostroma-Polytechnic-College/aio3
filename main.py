import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import load_dotenv

from bot import handlers
from bot.models.models import *


load_dotenv('.env')
token = os.getenv("TOKEN_API") or ""
bot = Bot(token=token, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

async def send_admin():
    await bot.send_message(320720102, "Бот запущен!")
    while True:
        await asyncio.sleep(10)
        await bot.send_message(320720102, "sleep")



async def main():

    handlers.include_routers(dp)
    
    try:
        dp.startup.register(send_admin)
        await dp.start_polling(bot, 
        allowed_updates=dp.resolve_used_update_types())
    except Exception as _ex:
        print(f'There is exception - {_ex}')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

    