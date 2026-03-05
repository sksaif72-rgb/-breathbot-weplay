import random
import string

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.config import ADMIN_ID
from bot.database import pool

router = Router()


def generate_code():

    return ''.join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=10
        )
    )


@router.message(Command("createcode"))
async def create_code(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    try:
        days = int(message.text.split()[1])
    except:
        await message.answer("اكتب عدد الايام\nمثال:\n/createcode 7")
        return

    code = generate_code()

    async with pool.acquire() as conn:

        await conn.execute(
            """
            INSERT INTO activation_codes(code,days)
            VALUES($1,$2)
            """,
            code,
            days
        )

    await message.answer(
        f"تم انشاء الكود\n\n{code}\n\nالمدة: {days} يوم"
    )
