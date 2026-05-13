from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


styles_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="casual"),
            KeyboardButton(text="классика")
        ],
        [
            KeyboardButton(text="sports chic")
        ],
        [
            KeyboardButton(text="вечерний")
        ],
        [
            KeyboardButton(text="назад")
        ]
    ],
    resize_keyboard=True
)