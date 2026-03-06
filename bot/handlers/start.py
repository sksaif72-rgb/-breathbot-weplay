from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from bot.database import add_user
from bot.keyboards.menus import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    add_user(user_id)

    await update.message.reply_text(
        "اهلا بك في BREATHBOT-Weplay\n\n"
        "ارسل كود الاشتراك"
    )


def register(application):

    application.add_handler(
        CommandHandler("start", start)
    )
