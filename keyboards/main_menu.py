from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="подобрать по цвету")
        ],
        [
            KeyboardButton(text="подобрать по стилю")
        ]
    ],
    resize_keyboard=True
)