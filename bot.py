import asyncio

from aiogram import Bot, Dispatcher, F

from aiogram.types import Message

from config import BOT_TOKEN

from keyboards.main_menu import main_keyboard
from keyboards.styles_kb import styles_keyboard
from keyboards.colors_kb import colors_keyboard

from aiogram.fsm.context import FSMContext
from states.user_states import ColorSelection

from handlers.start import router as start_router

from services.recommendations import (
    get_style_images,
    get_color_images
)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(start_router)

# главное меню
@dp.message(F.text == "подобрать по стилю")
async def choose_style(message: Message):

    await message.answer(  
        "выбери стиль:",
        reply_markup=styles_keyboard
    )

@dp.message(F.text.in_(["casual", "классика", "sports chic", "вечерний"]))
async def style_handler(message: Message):

    await message.answer(
        "вот тебе несколько образов 💅\nнадеюсь, ты найдёшь подходящий именно тебе"
    )

    media = get_style_images(message.text)

    await message.answer_media_group(media)


# кнопка "назад"
@dp.message(F.text == "назад")
async def back(message: Message, state: FSMContext):

    # очищаем состояние FSM
    await state.clear()

    await message.answer(
        "ты в главном меню 💅",
        reply_markup=main_keyboard
    )


# кнопка "подбор по цвету"
@dp.message(F.text == "подобрать по цвету")
async def choose_color(message: Message, state: FSMContext):

    await state.set_state(ColorSelection.first_color)

    await message.answer(
        "выбери первый цвет",
        reply_markup=colors_keyboard
    )


# выбор цвета 1
@dp.message(ColorSelection.first_color)
async def first_color(message: Message, state: FSMContext):

    await state.update_data(first_color=message.text)
    await state.set_state(ColorSelection.second_color)

    await message.answer("выбери второй цвет")


# выбор цвета 2
@dp.message(ColorSelection.second_color)
async def second_color(message: Message, state: FSMContext):

    await state.update_data(second_color=message.text)
    await state.set_state(ColorSelection.third_color)

    await message.answer("выбери третий цвет")


# выбор цвета 3 
@dp.message(ColorSelection.third_color)
async def third_color(message: Message, state: FSMContext):

    await state.update_data(third_color=message.text)

    data = await state.get_data()

    first = data["first_color"]
    second = data["second_color"]
    third = data["third_color"]

    await message.answer(
        f"твоя цветовая комбинация\n\n"
        f"{first} + {second} + {third}"
    )

    await message.answer(
        "держи пример образа с этой цветовой комбинацией\n"
        "надеюсь, тебе понравится💅"
    )

    media = get_color_images(first, second, third)

    await message.answer_media_group(media)

    await state.clear()


    # кнопка ""обо мне"
@dp.message(F.text == "обо мне")
async def about_me(message: Message, state: FSMContext):
    
    await message.answer(
        "привет, я твой помощник-стилист!\n" 
        "с моей помощью ты сможешь составлять себе стильные образы на любой случай.\n\n" 
        "выбери стиль и я покажу тебе варианты образов.\n\n"
        "либо ты можешь выбрать три цвета и я покажу тебе образы под выбранную тобой цветовую гамму.\n\n" 
        "буду рад помочь тебе💅"
    )
    await state.clear()


# запуск
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())