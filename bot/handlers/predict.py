from telegram import Update
from telegram.ext import CallbackContext, CallbackQueryHandler
from bot.keyboards.menus import card_numbers, card_types, next_predict
from bot.database import get_connection

predict_sessions = {}


# ======================
# بدء التخمين
# ======================

def start_predict(update: Update, context: CallbackContext):

    query = update.callback_query
    user_id = query.from_user.id

    predict_sessions[user_id] = {}

    query.message.reply_text(
        "اختر الورقة المكشوفة:",
        reply_markup=card_numbers()
    )


# ======================
# اختيار الرقم
# ======================

def select_card(update: Update, context: CallbackContext):

    query = update.callback_query
    user_id = query.from_user.id

    card = query.data.split("_")[1]

    predict_sessions[user_id]["card"] = card

    query.message.reply_text(
        "اختر نوع الورقة:",
        reply_markup=card_types()
    )


# ======================
# اختيار النوع
# ======================

def select_type(update: Update, context: CallbackContext):

    query = update.callback_query
    user_id = query.from_user.id

    card_type = query.data.split("_")[1]

    predict_sessions[user_id]["type"] = card_type

    result = calculate_prediction(
        predict_sessions[user_id]["card"],
        card_type
    )

    query.message.reply_text(
        result,
        reply_markup=next_predict()
    )


# ======================
# حساب الاحتمالات
# ======================

def calculate_prediction(card, card_type):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT right_attack, COUNT(*)
        FROM training_data
        WHERE card=%s AND type=%s
        GROUP BY right_attack
        """,
        (card, card_type)
    )

    rows = cursor.fetchall()

    if not rows:
        return "لا توجد بيانات تدريب كافية."

    total = sum(r[1] for r in rows)

    best = max(rows, key=lambda x: x[1])

    attack = best[0]
    percent = round((best[1] / total) * 100, 2)

    return f"""
🎯 التخمين المتوقع

الورقة: {card}
النوع: {card_type}

الضربة المتوقعة:
{attack}

نسبة النجاح:
{percent}%
"""


# ======================
# تسجيل الهاندلرز
# ======================

def register_predict_handlers(dispatcher):

    dispatcher.add_handler(
        CallbackQueryHandler(start_predict, pattern="predict")
    )

    dispatcher.add_handler(
        CallbackQueryHandler(select_card, pattern="card_")
    )

    dispatcher.add_handler(
        CallbackQueryHandler(select_type, pattern="type_")
    )
