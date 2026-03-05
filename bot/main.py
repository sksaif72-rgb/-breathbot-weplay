import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config import BOT_TOKEN
from bot.database import connect_db, create_tables

from handlers import start, guess, training, stats, admin


async def main():

    logging.basicConfig(level=logging.INFO)

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(guess.router)
    dp.include_router(training.router)
    dp.include_router(stats.router)
    dp.include_router(admin.router)

    await connect_db()
    await create_tables()

    print("BREATHBOT-Weplay running")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
