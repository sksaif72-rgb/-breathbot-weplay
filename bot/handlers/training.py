from telegram import Update
from telegram.ext import CallbackContext, CallbackQueryHandler
from datetime import datetime
import pytz

from bot.database import get_connection
from bot.keyboards.menus import card_numbers, card_types, right_attacks, left_attacks


# تخزين حالة التدريب مؤقتاً
training_sessions = {}


# =========================
# بدء التدريب
# =========================

def start_training(update: Update, context: CallbackContext):

    query = update.callback_query
    user_id = query.from_user.id

    training_sessions[user_id] = {}

    query.message.reply_text(
        "اختر رقم الورقة المكشوفة:",
        reply_markup=card_numbers()
    )


# =========================
# اختيار رقم الورقة
# =========================

def select_card(update: Update, context: CallbackContext):

    query = update.callback_query
    user_id = query.from_user.id

    card = query.data.split("_")[1]

    training_sessions[user_id]["card"] = card

    query.message.reply_text(
        "اختر نوع الورقة:",
        reply_markup=card_types()
    )


# =========================
# اختيار نوع الورقة
# =========================

def select_type(update: Update, context: CallbackContext):

    query = update.callback_query
    user_id = query.from_user.id

    card_type = query.data.split("_")[1]

    training_sessions[user_id]["type"] = card_type

    query.message.reply_text(
        "ماذا كانت ضربة اليمين؟",
        reply_markup=right_attacks()
    )


# =========================
# ضربة اليمين
# =========================

def select_right(update: Update, context: CallbackContext):

    query = update.callback_query
    user_id = query.from_user.id

    attack = query.data.replace("r_", "")

    training_sessions[user_id]["right"] = attack

    query.message.reply_text(
        "ماذا كانت ضربة اليسار؟",
        reply_markup=left_attacks()
    )


# =========================
# ضربة اليسار
# =========================

def select_left(update: Update, context: CallbackContext):

    query = update.callback_query
    user_id = query.from_user.id

    attack = query.data.replace("l_", "")

    training_sessions[user_id]["left"] = attack

    # وقت الرياض
    riyadh = pytz.timezone("Asia/Riyadh")
    minute = datetime.now(riyadh).minute

    session = training_sessions[user_id]

    save_training(
        session["card"],
        session["type"],
        minute,
        session["right"],
        session["left"]
    )

    query.message.reply_text(
        f"""
✅ تم حفظ التدريب

الورقة: {session['card']}
النوع: {session['type']}
الدقيقة: {minute}

يمين: {session['right']}
يسار: {session['left']}
"""
    )

    training_sessions.pop(user_id)


# =========================
# حفظ البيانات
# =========================

def save_training(card, card_type, minute, right_attack, left_attack):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO training_data
        (card, type, minute, right_attack, left_attack)
        VALUES (%s,%s,%s,%s,%s)
        """,
        (card, card_type, minute, right_attack, left_attack)
    )

    conn.commit()

    cursor.close()
    conn.close()


# =========================
# تسجيل الهاندلرز
# =========================

def register_training_handlers(dispatcher):

    dispatcher.add_handler(CallbackQueryHandler(start_training, pattern="training"))

    dispatcher.add_handler(CallbackQueryHandler(select_card, pattern="card_"))

    dispatcher.add_handler(CallbackQueryHandler(select_type, pattern="type_"))

    dispatcher.add_handler(CallbackQueryHandler(select_right, pattern="r_"))

    dispatcher.add_handler(CallbackQueryHandler(select_left, pattern="l_"))
