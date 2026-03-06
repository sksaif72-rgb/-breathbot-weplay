from telegram.ext import ApplicationBuilder

from bot.config import BOT_TOKEN

from bot.handlers import start
from bot.handlers import guess
from bot.handlers import training
from bot.handlers import stats
from bot.handlers import admin


async def main():

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start.register(application)
    guess.register(application)
    training.register(application)
    stats.register(application)
    admin.register(application)

    print("BREATHBOT-Weplay started")

    await application.run_polling()


if __name__ == "__main__":

    import asyncio
    asyncio.run(main())
