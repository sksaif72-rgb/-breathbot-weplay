from telegram import ReplyKeyboardMarkup


def main_menu_keyboard():
    keyboard = [
        ["🎯 بدء التخمين"],
        ["📊 الاحصائيات"],
        ["🧠 وضع التدريب"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# أرقام الأوراق
def card_numbers():
    keyboard = [
        ["A", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "J", "Q"],
        ["K"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# أنواع الورق
def card_types():
    keyboard = [
        ["♠️ سنك", "♥️ قلب"],
        ["♦️ دينار", "♣️ ماجة"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# ضربات اليمين
def right_attacks():
    keyboard = [
        ["زوجين"],
        ["متتالية"],
        ["ثلاثة"],
        ["فل هاوس"],
        ["اربعة"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# ضربات اليسار
def left_attacks():
    keyboard = [
        ["زوج"],
        ["متتالية نفس النوع"],
        ["AA"],
        ["زوج + متتالية"],
        ["لاشيء"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
