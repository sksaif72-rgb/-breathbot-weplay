from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
keyboard=[
[KeyboardButton(text="بدء التخمين")],
[KeyboardButton(text="الاحصائيات")],
[KeyboardButton(text="حسابي")],
[KeyboardButton(text="تواصل مع الدعم")]
],
resize_keyboard=True
)
