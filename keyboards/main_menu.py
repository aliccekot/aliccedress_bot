# импортируем классы для создания клавиатуры бота
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup( # cоздаём объект клавиатуры main_keyboard
    keyboard=[
        [
            KeyboardButton(text="подобрать по цвету") # первая строка
        ],
        [
            KeyboardButton(text="подобрать по стилю") # вторая строка
        ],
        [
            KeyboardButton(text="обо мне"), # третья строка
        ] 
    ],
    resize_keyboard=True  # автоматически уменьшает размер клавиатуры, делая удобной для пользователя
)