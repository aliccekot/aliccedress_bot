from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


colors_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="бежевый"),
            KeyboardButton(text="белый"),
            KeyboardButton(text="голубой")
        ],
        [
            KeyboardButton(text="желтый"),
            KeyboardButton(text="зеленый"),
            KeyboardButton(text="коричневый")
        ],
        [
            KeyboardButton(text="красный"),
            KeyboardButton(text="оранжевый"),
            KeyboardButton(text="розовый")
        ],
        [
            KeyboardButton(text="серый"),
            KeyboardButton(text="синий"),
            KeyboardButton(text="фиолетовый")
        ],
        [
            KeyboardButton(text="черный")
        ],
        [
            KeyboardButton(text="назад")
        ]
    ],
    resize_keyboard=True
)