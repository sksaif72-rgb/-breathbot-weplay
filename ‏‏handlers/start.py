from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.database import pool
from keyboards.menus import main_menu

router = Router()


@router.message(Command("start"))
async def start(message: Message):

    telegram_id = message.from_user.id
    username = message.from_user.username

    async with pool.acquire() as conn:

        await conn.execute(
            """
            INSERT INTO users(telegram_id, username)
            VALUES($1,$2)
            ON CONFLICT(telegram_id) DO NOTHING
            """,
            telegram_id,
            username
        )

    await message.answer(
        "مرحبا بك في BREATHBOT-Weplay\n\n"
        "اكتب كود الاشتراك"
    )
