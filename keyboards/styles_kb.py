# импортируем классы для создания клавиатуры бота
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


styles_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="casual"), # первая строка
            KeyboardButton(text="классика")
        ],
        [
            KeyboardButton(text="sports chic") # вторая строка
        ],
        [
            KeyboardButton(text="вечерний") # третья строка
        ],
        [
            KeyboardButton(text="назад") # четвертая строка
        ]
    ],
    resize_keyboard=True # автоматически уменьшает размер клавиатуры, делая удобной для пользователя
)