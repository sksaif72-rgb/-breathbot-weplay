from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cards = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]

types = ["سِنك","دينار","قلب","ماجه"]

right_results = [
"زوجين",
"متتالية",
"ثلاثة",
"فل هاوس",
"اربعة"
]

left_results = [
"زوج",
"متتالية نفس النوع",
"AA",
"زوج و متتالية",
"لاشيء"
]


def training_cards_keyboard():

    keyboard = []
    row = []

    for card in cards:

        row.append(
            InlineKeyboardButton(
                text=card,
                callback_data=f"tcard_{card}"
            )
        )

        if len(row) == 4:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def training_types_keyboard():

    keyboard = []

    for t in types:

        keyboard.append([
            InlineKeyboardButton(
                text=t,
                callback_data=f"ttype_{t}"
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def right_results_keyboard():

    keyboard = []

    for r in right_results:

        keyboard.append([
            InlineKeyboardButton(
                text=r,
                callback_data=f"right_{r}"
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def left_results_keyboard():

    keyboard = []

    for r in left_results:

        keyboard.append([
            InlineKeyboardButton(
                text=r,
                callback_data=f"left_{r}"
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
