from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes, MessageHandler, filters


# قائمة الأرقام A → K
cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

# أنواع الورق
suits = ["سنك", "دينار", "قلب", "ماجة"]


def card_keyboard():
    keyboard = []
    row = []

    for c in cards:
        row.append(KeyboardButton(c))
        if len(row) == 4:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def suit_keyboard():
    keyboard = [[KeyboardButton(s)] for s in suits]

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# عند الضغط على زر التخمين
async def guess_start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text != "🎯 تخمين":
        return

    await update.message.reply_text(
        "اختر رقم الورقة",
        reply_markup=card_keyboard()
    )


# بعد اختيار الرقم
async def receive_card(update: Update, context: ContextTypes.DEFAULT_TYPE):

    card = update.message.text

    if card not in cards:
        return

    context.user_data["card"] = card

    await update.message.reply_text(
        "اختر نوع الورقة",
        reply_markup=suit_keyboard()
    )


# بعد اختيار النوع
async def receive_suit(update: Update, context: ContextTypes.DEFAULT_TYPE):

    suit = update.message.text

    if suit not in suits:
        return

    card = context.user_data.get("card")

    await update.message.reply_text(
        f"🔮 التخمين للورقة\n\n"
        f"{card} {suit}\n\n"
        f"النتيجة المتوقعة:\n"
        f"يمين: زوجين 60%\n"
        f"يسار: زوج 40%"
    )


def register(application):

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, guess_start)
    )

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, receive_card)
    )

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, receive_suit)
    )
