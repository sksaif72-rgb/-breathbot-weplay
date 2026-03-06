from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def right_results_keyboard():

    results = [
        "زوجين",
        "متتالية",
        "ثلاثة",
        "فل هاوس",
        "اربعة"
    ]

    keyboard = []

    for r in results:

        keyboard.append([
            InlineKeyboardButton(
                text=r,
                callback_data=f"right_{r}"
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def left_results_keyboard():

    results = [
        "زوج",
        "متتالية نفس النوع",
        "AA",
        "زوج و متتالية",
        "لاشيء"
    ]

    keyboard = []

    for r in results:

        keyboard.append([
            InlineKeyboardButton(
                text=r,
                callback_data=f"left_{r}"
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
