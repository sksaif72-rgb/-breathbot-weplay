from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():

    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.add(
        KeyboardButton("🎯 تخمين"),
        KeyboardButton("📊 احصائيات")
    )

    return kb


def training_menu():

    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.add(
        KeyboardButton("AA"),
        KeyboardButton("اربعة"),
        KeyboardButton("فل هاوس"),
        KeyboardButton("زوج"),
        KeyboardButton("متتالية"),
        KeyboardButton("لا شيء")
    )

    return kb
