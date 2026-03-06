from aiogram import types
from aiogram.dispatcher import Dispatcher

from bot.database import add_user
from bot.keyboards.menus import main_menu


async def start(message: types.Message):

    await add_user(message.from_user.id)

    await message.answer(
        "اهلا بك في BREATHBOT-Weplay",
        reply_markup=main_menu()
    )


def register(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
