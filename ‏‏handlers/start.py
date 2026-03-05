from aiogram import Router
from aiogram.types import Message
from keyboards.menus import menu

router = Router()

@router.message(commands=["start"])
async def start(msg: Message):

    await msg.answer(
        "اهلاً بك في BREATHBOT-Weplay\n\nاكتب كود الاشتراك"
    )
