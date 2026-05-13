from aiogram import Router # импортируем класс Router
# он используется для обработки команд и сообщений пользователя

from aiogram.filters import CommandStart # импортируем фильтр CommandStart
# он позволяет боту реагировать на команду /start

from aiogram.types import Message # импортируем тип Message
# Message представляет сообщение, которое отправил пользователь


from keyboards.main_menu import main_keyboard # импортируем клавиатуру главного меню (main_keyboard)    


router = Router() # через него будут регистрироваться обработчики сообщений



# когда пользователь вводит команду /start
# выполняется функция start()
@router.message(CommandStart())
async def start(message: Message):

    # await — позволяет ждать выполнения асинхронной операции
    await message.answer(   # message.answer() используется для отправки текста в чат
        "привет!\n"
        "я бот для подбора образов. "
        "подберу тебе идеальный образ на основе твоих предпочтений 💅\n\n"
        "что ты хочешь выбрать сегодня?",
        reply_markup=main_keyboard # подключаем клавиатуру с кнопками, выходим на главное меню бота
    )
