from aiogram import types
from aiogram.dispatcher import Dispatcher

from bot.config import ADMIN_ID
from bot.database import pool


async def broadcast(message: types.Message):

    if message.from_user.id != ADMIN_ID:
        return

    text = message.get_args()

    async with pool.acquire() as conn:
        users = await conn.fetch("SELECT user_id FROM users")

    for u in users:

        try:
            await message.bot.send_message(u["user_id"], text)
        except:
            pass


def register(dp: Dispatcher):

    dp.register_message_handler(
        broadcast,
        commands=["broadcast"]
    )
