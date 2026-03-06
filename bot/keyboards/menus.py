from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


# القائمة الرئيسية
def main_menu_keyboard():
    keyboard = [
        ["🎯 بدء التخمين"],
        ["📊 الاحصائيات"],
        ["🧠 وضع التدريب"]
    ]

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# اختيار رقم الورقة
def card_number_keyboard():

    numbers = [
        ["A", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "J", "Q"],
        ["K"]
    ]

    return ReplyKeyboardMarkup(numbers, resize_keyboard=True)


# اختيار نوع الورقة
def card_type_keyboard():

    types = [
        ["♠️ سنك", "♥️ قلب"],
        ["♦️ دينار", "♣️ ماجة"]
    ]

    return ReplyKeyboardMarkup(types, resize_keyboard=True)


# ضربات اليمين
def right_hits_keyboard():

    keyboard = [
        ["زوجين"],
        ["متتالية"],
        ["ثلاثة"],
        ["فل هاوس"],
        ["اربعة"]
    ]

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# ضربات اليسار (وضع التدريب)
def left_hits_keyboard():

    keyboard = [
        ["زوج"],
        ["متتالية نفس النوع"],
        ["AA"],
        ["زوج + متتالية"],
        ["لاشيء"]
    ]

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
