from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from bot.database import pool

from keyboards.training import (
    training_cards_keyboard,
    training_types_keyboard,
    right_results_keyboard,
    left_results_keyboard
)

router = Router()

trainer_state = {}


async def is_trainer(user_id):

    async with pool.acquire() as conn:

        row = await conn.fetchrow(
            "SELECT * FROM trainers WHERE telegram_id=$1",
            user_id
        )

    return row is not None


@router.message(Command("training"))
async def start_training(message: Message):

    if not await is_trainer(message.from_user.id):

        await message.answer("هذا الوضع للمدربين فقط")
        return

    trainer_state[message.from_user.id] = {}

    await message.answer(
        "اختر الورقة",
        reply_markup=training_cards_keyboard()
    )


@router.callback_query(lambda c: c.data.startswith("tcard_"))
async def choose_card(callback: CallbackQuery):

    card = callback.data.split("_")[1]

    trainer_state[callback.from_user.id]["card"] = card

    await callback.message.answer(
        "اختر نوع الورقة",
        reply_markup=training_types_keyboard()
    )


@router.callback_query(lambda c: c.data.startswith("ttype_"))
async def choose_type(callback: CallbackQuery):

    type_ = callback.data.split("_")[1]

    trainer_state[callback.from_user.id]["type"] = type_

    await callback.message.answer(
        "ماذا ضرب في اليمين؟",
        reply_markup=right_results_keyboard()
    )


@router.callback_query(lambda c: c.data.startswith("right_"))
async def choose_right(callback: CallbackQuery):

    right = callback.data.split("_",1)[1]

    trainer_state[callback.from_user.id]["right"] = right

    await callback.message.answer(
        "ماذا ضرب في اليسار؟",
        reply_markup=left_results_keyboard()
    )


@router.callback_query(lambda c: c.data.startswith("left_"))
async def choose_left(callback: CallbackQuery):

    left = callback.data.split("_",1)[1]

    data = trainer_state[callback.from_user.id]

    card = data["card"]
    type_ = data["type"]
    right = data["right"]

    from datetime import datetime
    import pytz

    riyadh = pytz.timezone("Asia/Riyadh")

    minute = datetime.now(riyadh).minute

    async with pool.acquire() as conn:

        await conn.execute(
            """
            INSERT INTO training_data
            (card,type,minute,right_result,left_result)
            VALUES($1,$2,$3,$4,$5)
            """,
            card,
            type_,
            minute,
            right,
            left
        )

    await callback.message.answer(
        "تم حفظ التدريب ✅"
    )

    trainer_state.pop(callback.from_user.id, None)
