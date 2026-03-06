from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, filters
from bot.keyboards.menus import main_menu_keyboard


def start(update: Update, context: CallbackContext):
    user = update.effective_user

    text = f"""
اهلا بك {user.first_name}

مرحبا بك في بوت BREATHBOT-Weplay

اختر من القائمة:
"""

    update.message.reply_text(
        text,
        reply_markup=main_menu_keyboard()
    )


def register_start_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
