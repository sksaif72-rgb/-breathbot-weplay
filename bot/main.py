import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config import BOT_TOKEN
from bot.database import connect_db, create_tables

# handlers
from handlers import start
from handlers import guess
from handlers import training
from handlers import stats
from handlers import admin


async def main():

    # logs
    logging.basicConfig(level=logging.INFO)

    # bot
    bot = Bot(token=BOT_TOKEN)

    # dispatcher
    dp = Dispatcher()

    # connect database
    await connect_db()

    # create tables if not exist
    await create_tables()

    # register routers
    dp.include_router(start.router)
    dp.include_router(guess.router)
    dp.include_router(training.router)
    dp.include_router(stats.router)
    dp.include_router(admin.router)

    print("BREATHBOT-Weplay is running...")

    # start bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
