import asyncio

from aiogram import Bot, Dispatcher

from bot.config import BOT_TOKEN
from bot.database import connect

from handlers import start

bot = Bot(BOT_TOKEN)

dp = Dispatcher()

dp.include_router(start.router)

async def main():

    await connect()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
