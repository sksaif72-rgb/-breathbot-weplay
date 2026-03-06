import asyncio

from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from .config import BOT_TOKEN
from .database import connect

from handlers import start, guess, training, stats, admin


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


async def on_startup(dp):

    await connect()

    start.register(dp)
    guess.register(dp)
    training.register(dp)
    stats.register(dp)
    admin.register(dp)

    print("BOT STARTED")


if __name__ == "__main__":

    executor.start_polling(
        dp,
        on_startup=on_startup
    )
