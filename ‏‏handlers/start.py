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
@router.message()
async def activate_code(message: Message):

    code = message.text.strip()

    async with pool.acquire() as conn:

        row = await conn.fetchrow(
            "SELECT * FROM activation_codes WHERE code=$1 AND used=false",
            code
        )

        if not row:
            await message.answer("الكود غير صحيح")
            return

        days = row["days"]

        await conn.execute(
            "UPDATE activation_codes SET used=true, used_by=$1 WHERE code=$2",
            message.from_user.id,
            code
        )

        user = await conn.fetchrow(
            "SELECT id FROM users WHERE telegram_id=$1",
            message.from_user.id
        )

        await conn.execute(
            """
            INSERT INTO subscriptions(user_id,expire_at)
            VALUES($1,NOW() + ($2 || ' days')::interval)
            """,
            user["id"],
            days
        )

    await message.answer(
        f"تم التفعيل ✅\n\n"
        f"مدة الاشتراك: {days} يوم",
        reply_markup=main_menu()
    )
