from aiogram import types
from aiogram.dispatcher import Dispatcher

from bot.config import TRAINING_CODE
from bot.database import add_training
from keyboards.menus import training_menu

import datetime


async def enter_training(message: types.Message):

    if message.text == TRAINING_CODE:

        await message.answer(
            "تم الدخول لوضع التدريب",
            reply_markup=training_menu()
        )


async def save_training(message: types.Message):

    hand = message.text

    minute = datetime.datetime.now().minute

    card = "unknown"
    suit = "unknown"

    await add_training(card, suit, hand, minute)

    await message.answer("تم حفظ التدريب")


def register(dp: Dispatcher):

    dp.register_message_handler(enter_training)

    dp.register_message_handler(
        save_training,
        lambda m: m.text in [
            "AA",
            "اربعة",
            "فل هاوس",
            "زوج",
            "متتالية",
            "لا شيء"
        ]
    )
