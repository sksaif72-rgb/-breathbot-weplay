from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters


async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text != "🎯 تخمين":
        return

    await update.message.reply_text(
        "اختر الورقة"
    )


def register(application):

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, guess)
    )
