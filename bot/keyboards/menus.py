from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# =========================
# القائمة الرئيسية
# =========================

def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("🎯 بدء التخمين", callback_data="predict")
        ],
        [
            InlineKeyboardButton("📊 الإحصائيات", callback_data="stats")
        ],
        [
            InlineKeyboardButton("🎓 وضع التدريب", callback_data="training")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================
# اختيار رقم الورقة
# =========================

def card_numbers():
    keyboard = [
        [
            InlineKeyboardButton("A", callback_data="card_A"),
            InlineKeyboardButton("2", callback_data="card_2"),
            InlineKeyboardButton("3", callback_data="card_3"),
            InlineKeyboardButton("4", callback_data="card_4")
        ],
        [
            InlineKeyboardButton("5", callback_data="card_5"),
            InlineKeyboardButton("6", callback_data="card_6"),
            InlineKeyboardButton("7", callback_data="card_7"),
            InlineKeyboardButton("8", callback_data="card_8")
        ],
        [
            InlineKeyboardButton("9", callback_data="card_9"),
            InlineKeyboardButton("10", callback_data="card_10"),
            InlineKeyboardButton("J", callback_data="card_J"),
            InlineKeyboardButton("Q", callback_data="card_Q")
        ],
        [
            InlineKeyboardButton("K", callback_data="card_K")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================
# اختيار نوع الورقة
# =========================

def card_types():
    keyboard = [
        [
            InlineKeyboardButton("♠️ سنك", callback_data="type_spade"),
            InlineKeyboardButton("♦️ دينار", callback_data="type_dinar")
        ],
        [
            InlineKeyboardButton("♥️ قلب", callback_data="type_heart"),
            InlineKeyboardButton("♣️ ماجة", callback_data="type_maja")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================
# ضربات اليمين
# =========================

def right_attacks():
    keyboard = [
        [InlineKeyboardButton("زوجين", callback_data="r_two_pair")],
        [InlineKeyboardButton("متتالية", callback_data="r_straight")],
        [InlineKeyboardButton("ثلاثة", callback_data="r_three")],
        [InlineKeyboardButton("فل هاوس", callback_data="r_fullhouse")],
        [InlineKeyboardButton("أربعة", callback_data="r_four")]
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================
# ضربات اليسار
# =========================

def left_attacks():
    keyboard = [
        [InlineKeyboardButton("زوج", callback_data="l_pair")],
        [InlineKeyboardButton("متتالية نفس النوع", callback_data="l_straight_flush")],
        [InlineKeyboardButton("AA", callback_data="l_aa")],
        [InlineKeyboardButton("زوج + متتالية", callback_data="l_pair_sequence")],
        [InlineKeyboardButton("لا شيء", callback_data="l_none")]
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================
# زر التخمين التالي
# =========================

def next_predict():
    keyboard = [
        [
            InlineKeyboardButton("🔁 التخمين التالي", callback_data="next_predict")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================
# قائمة الاحصائيات
# =========================

def stats_menu():
    keyboard = [
        [
            InlineKeyboardButton("📊 احصائيات ورقة", callback_data="stats_card")
        ],
        [
            InlineKeyboardButton("⏱ افضل دقيقة", callback_data="best_minute")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
