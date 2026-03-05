from aiogram import Router
from aiogram.types import CallbackQuery

from bot.database import pool

router = Router()


@router.callback_query(lambda c: c.data == "stats")
async def stats(callback: CallbackQuery):

    async with pool.acquire() as conn:

        rows = await conn.fetch(
            """
            SELECT card,type,COUNT(*) as c
            FROM training_data
            GROUP BY card,type
            ORDER BY c DESC
            LIMIT 10
            """
        )

    text = "اكثر البيانات المسجلة:\n\n"

    for r in rows:

        text += f"{r['card']} {r['type']} : {r['c']}\n"

    await callback.message.answer(text)
