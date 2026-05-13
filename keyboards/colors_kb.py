# импортируем классы для создания клавиатуры бота
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


colors_keyboard = ReplyKeyboardMarkup(  # cоздаём объект клавиатуры colors_keyboard
    keyboard=[
        [
            KeyboardButton(text="бежевый"), # первая строка
            KeyboardButton(text="белый"),
            KeyboardButton(text="голубой")
        ],
        [
            KeyboardButton(text="желтый"), # вторая строка
            KeyboardButton(text="зеленый"),
            KeyboardButton(text="коричневый")
        ],
        [ 
            KeyboardButton(text="красный"), # третья строка
            KeyboardButton(text="оранжевый"),
            KeyboardButton(text="розовый")
        ],
        [
            KeyboardButton(text="серый"), # четвертая строка
            KeyboardButton(text="синий"),
            KeyboardButton(text="фиолетовый")
        ],
        [
            KeyboardButton(text="черный") # пятая строка
        ],
        [
            KeyboardButton(text="назад") # шестая строка
        ]
    ], 
    resize_keyboard=True # автоматически уменьшает размер клавиатуры, делая удобной для пользователя
)