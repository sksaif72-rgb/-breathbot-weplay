from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters
from bot.keyboards.menus import main_menu
from bot.database import get_connection
from datetime import datetime


waiting_code = {}


# ======================
# /start
# ======================

def start(update: Update, context: CallbackContext):

    user_id = update.effective_user.id

    waiting_code[user_id] = True

    update.message.reply_text(
        "🔐 مرحباً بك في BREATHBOT-Weplay\n\n"
        "اكتب كود الاشتراك لتفعيل البوت:"
    )


# ======================
# استقبال الكود
# ======================

def receive_code(update: Update, context: CallbackContext):

    user_id = update.effective_user.id

    if user_id not in waiting_code:
        return

    code = update.message.text.strip()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT duration FROM subscription_codes WHERE code=%s",
        (code,)
    )

    result = cursor.fetchone()

    if not result:

        update.message.reply_text("❌ الكود غير صحيح")
        return

    duration = result[0]

    expire_date = datetime.now().timestamp() + (duration * 86400)

    cursor.execute(
        """
        INSERT INTO users (user_id, expire_date)
        VALUES (%s,%s)
        ON CONFLICT (user_id)
        DO UPDATE SET expire_date=%s
        """,
        (user_id, expire_date, expire_date)
    )

    conn.commit()

    cursor.execute(
        "DELETE FROM subscription_codes WHERE code=%s",
        (code,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    update.message.reply_text(
        f"""
✅ جاري التفعيل...

🔥 المود شغال

مدة الاشتراك:
{duration} يوم
""",
        reply_markup=main_menu()
    )

    waiting_code.pop(user_id)


# ======================
# تسجيل الهاندلرز
# ======================

def register_start_handlers(dispatcher):

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, receive_code)
    )
