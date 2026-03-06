from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters


async def training(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text != "🎓 وضع التدريب":
        return

    await update.message.reply_text(
        "وضع التدريب مفعل"
    )


def register(application):

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, training)
    )
