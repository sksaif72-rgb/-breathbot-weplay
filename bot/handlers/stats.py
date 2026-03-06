from aiogram import types
from aiogram.dispatcher import Dispatcher

from bot.database import get_stats


async def stats(message: types.Message):

    await message.answer("اكتب رقم الورقة مثال: 7")


async def stats_card(message: types.Message):

    card = message.text

    rows = await get_stats(card)

    text = "📊 الاحصائيات\n\n"

    for r in rows:

        text += f"{r['suit']} - {r['hand_type']} : {r['c']}\n"

    await message.answer(text)


def register(dp: Dispatcher):

    dp.register_message_handler(
        stats,
        lambda m: m.text == "📊 احصائيات"
    )

    dp.register_message_handler(stats_card)
