from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.cards import cards_keyboard, type_keyboard
from ai.predictor import predict_move

router = Router()

user_state = {}


@router.callback_query(lambda c: c.data == "start_guess")
async def start_guess(callback: CallbackQuery):

    await callback.message.answer(
        "اختر الورقة",
        reply_markup=cards_keyboard()
    )


@router.callback_query(lambda c: c.data.startswith("card_"))
async def choose_card(callback: CallbackQuery):

    card = callback.data.split("_")[1]

    user_state[callback.from_user.id] = {"card": card}

    await callback.message.answer(
        "اختر نوع الورقة",
        reply_markup=type_keyboard()
    )


@router.callback_query(lambda c: c.data.startswith("type_"))
async def choose_type(callback: CallbackQuery):

    t = callback.data.split("_")[1]

    user_state[callback.from_user.id]["type"] = t

    card = user_state[callback.from_user.id]["card"]

    prediction = await predict_move(card, t)

    await callback.message.answer(
        f"التخمين المتوقع:\n\n"
        f"{prediction['result']}\n\n"
        f"النسبة: {prediction['prob']}%"
    )
