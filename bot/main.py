import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config import BOT_TOKEN
from bot.database import connect_db, create_tables

from handlers import start
from handlers import guess
from handlers import training
from handlers import stats
from handlers import admin

from bot.scheduler import start_scheduler


async def main():

    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()

    # تسجيل الهاندلرز
    dp.include_router(start.router)
    dp.include_router(guess.router)
    dp.include_router(training.router)
    dp.include_router(stats.router)
    dp.include_router(admin.router)

    # الاتصال بقاعدة البيانات
    await connect_db()

    # إنشاء الجداول اذا لم تكن موجودة
    await create_tables()

    print("BREATHBOT-Weplay started")

    # تشغيل Scheduler
    start_scheduler(bot)

    # تشغيل البوت
    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(main())
