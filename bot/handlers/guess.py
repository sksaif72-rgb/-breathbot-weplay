from aiogram import types
from aiogram.dispatcher import Dispatcher

from bot.ai.predictor import predict


async def guess(message: types.Message):

    await message.answer("اكتب الورقة مثال:\n7 قلب")


async def process_guess(message: types.Message):

    data = message.text.split()

    if len(data) != 2:
        return

    card = data[0]
    suit = data[1]

    result = await predict(card, suit)

    await message.answer(f"التخمين: {result}")


def register(dp: Dispatcher):

    dp.register_message_handler(
        guess,
        lambda m: m.text == "🎯 تخمين"
    )

    dp.register_message_handler(process_guess)
