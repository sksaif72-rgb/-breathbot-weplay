from aiogram import Router
from aiogram.types import Message

from bot.database import pool

router = Router()


@router.message(lambda m: m.text == "/training")
async def start_training(message: Message):

    await message.answer(
        "اكتب البيانات بهذا الشكل:\n\n"
        "card type minute right left\n\n"
        "مثال:\n"
        "9 دينار 44 زوجين زوج"
    )


@router.message(lambda m: len(m.text.split()) == 5)
async def save_training(message: Message):

    card, type_, minute, right, left = message.text.split()

    async with pool.acquire() as conn:

        await conn.execute(
            """
            INSERT INTO training_data
            (card,type,minute,right_result,left_result)
            VALUES($1,$2,$3,$4,$5)
            """,
            card,
            type_,
            int(minute),
            right,
            left
        )

    await message.answer("تم حفظ التدريب")
