from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text != "📊 احصائيات":
        return

    await update.message.reply_text(
        "لوحة الاحصائيات"
    )


def register(application):

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, stats)
    )
