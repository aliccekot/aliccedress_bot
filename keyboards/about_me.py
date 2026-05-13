# импортируем классы для создания клавиатуры бота
# ReplyKeyboardMarkup отвечает за создание клавиатуры
# KeyboardButton отвечает за создание отдельной кнопки

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


about_me_keyboard = ReplyKeyboardMarkup( # cоздаём объект клавиатуры about_me_keyboard
    keyboard=[
        [
            KeyboardButton(text="обо мне")
        ],
    ],
    resize_keyboard=True # автоматически уменьшает размер клавиатуры, делая удобной для пользователя
)