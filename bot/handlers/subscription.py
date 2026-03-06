from telegram.ext import CommandHandler

def subscription(update, context):
    update.message.reply_text("📌 نظام الاشتراك سيضاف قريباً.")

def register_subscription_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("subscribe", subscription))
