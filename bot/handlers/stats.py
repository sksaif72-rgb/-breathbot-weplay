from telegram.ext import CommandHandler
from bot.database import get_card_stats


def stats_command(update, context):
    update.message.reply_text("📊 ارسل رقم الورقة لمعرفة الاحصائيات (مثال: 7)")


def card_stats(update, context):
    card = update.message.text

    stats = get_card_stats(card)

    if not stats:
        update.message.reply_text("لا توجد بيانات لهذا الرقم بعد.")
        return

    text = f"📊 احصائيات الورقة {card}\n\n"

    for row in stats:
        text += f"{row['type']} → {row['right_attack']} ({row['count']} مرة)\n"

    update.message.reply_text(text)


def register_stats_handlers(dispatcher):

    dispatcher.add_handler(CommandHandler("stats", stats_command))
