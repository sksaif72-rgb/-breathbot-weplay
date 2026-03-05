from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="بدء التخمين",
                    callback_data="start_guess"
                )
            ],

            [
                InlineKeyboardButton(
                    text="الاحصائيات",
                    callback_data="stats"
                )
            ]

        ]
    )
