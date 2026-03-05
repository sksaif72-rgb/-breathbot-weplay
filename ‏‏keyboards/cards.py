from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cards = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]

types = ["سِنك","دينار","قلب","ماجه"]


def cards_keyboard():

    keyboard = []

    row = []

    for i, card in enumerate(cards):

        row.append(
            InlineKeyboardButton(
                text=card,
                callback_data=f"card_{card}"
            )
        )

        if len(row) == 4:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def type_keyboard():

    keyboard = []

    for t in types:

        keyboard.append([
            InlineKeyboardButton(
                text=t,
                callback_data=f"type_{t}"
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
