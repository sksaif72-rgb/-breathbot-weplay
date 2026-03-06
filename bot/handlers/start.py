from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters

from bot.database import add_user
from bot.keyboards.menus import main_menu


# عند كتابة /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user
    user_id = user.id

    # حفظ المستخدم في قاعدة البيانات
    add_user(user_id)

    await update.message.reply_text(
        "اهلاً بك في BREATHBOT-Weplay\n\n"
        "🔐 ارسل كود الاشتراك لتفعيل البوت",
    )


# استقبال كود الاشتراك
async def receive_code(update: Update, context: ContextTypes.DEFAULT_TYPE):

    code = update.message.text

    # حاليا مجرد تجربة
    # لاحقاً سنربطه بقاعدة البيانات

    await update.message.reply_text(
        "⏳ جاري التفعيل ...",
    )

    await update.message.reply_text(
        "✅ تم تفعيل الاشتراك\n"
        "📅 المدة المتبقية: 30 يوم",
        reply_markup=main_menu()
    )


# تسجيل الهاندلرز في البوت
def register(application):

    application.add_handler(CommandHandler("start", start))

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            receive_code
        )
    )
