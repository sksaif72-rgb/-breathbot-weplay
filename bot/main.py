import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from aiohttp import web

from bot.config import BOT_TOKEN
from bot.database import connect_db

from handlers import start, guess, training, stats, admin


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


# -----------------------
# WEB SERVER FOR RENDER
# -----------------------

async def health(request):
    return web.Response(text="BREATHBOT RUNNING")


async def start_web_server():
    port = int(os.environ.get("PORT", 10000))

    app = web.Application()
    app.router.add_get("/", health)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    print(f"Web server started on port {port}")


# -----------------------
# STARTUP
# -----------------------

async def on_startup(dp):

    print("Connecting database...")
    await connect_db()

    print("Starting web server...")
    asyncio.create_task(start_web_server())

    print("Bot started successfully")


# -----------------------
# REGISTER HANDLERS
# -----------------------

start.router.register(dp)
guess.router.register(dp)
training.router.register(dp)
stats.router.register(dp)
admin.router.register(dp)


# -----------------------
# MAIN
# -----------------------

if __name__ == "__main__":

    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
