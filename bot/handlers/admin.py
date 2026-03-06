from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text != "admin":
        return

    await update.message.reply_text(
        "لوحة الادمن"
    )


def register(application):

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, admin)
    )
