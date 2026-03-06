from telegram import ReplyKeyboardMarkup, KeyboardButton


def main_menu():

    keyboard = [
        [
            KeyboardButton("🎯 تخمين"),
            KeyboardButton("📊 احصائيات")
        ]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


def training_menu():

    keyboard = [
        [KeyboardButton("AA"), KeyboardButton("اربعة")],
        [KeyboardButton("فل هاوس"), KeyboardButton("زوج")],
        [KeyboardButton("متتالية"), KeyboardButton("لا شيء")]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
