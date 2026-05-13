import asyncio
import os
from aiogram.types import Message, FSInputFile, InputMediaPhoto

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from config import BOT_TOKEN
from keyboards.main_menu import main_keyboard
from keyboards.styles_kb import styles_keyboard
from aiogram.fsm.context import FSMContext

from keyboards.colors_kb import colors_keyboard

from states.user_states import ColorSelection

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Команда /start
@dp.message(CommandStart())
async def start(message: Message):

    await message.answer(
        "привет!\n"
        "я бот для подбора образов. подберу тебе идеальный образ на основе твоих предпочтений.\n\n"
        "что ты хочешь выбрать сегодня?💅",
        reply_markup=main_keyboard
    )


# Кнопка "Подбор по стилю"
@dp.message(F.text == "подобрать по стилю")
async def choose_style(message: Message):

    await message.answer(
        "выбери стиль одежды:",
        reply_markup=styles_keyboard
    )

# Casual
@dp.message(F.text == "casual")
async def casual_style(message: Message):

    await message.answer(
        "вот тебе несколько образов💅\n"
        "надеюсь, ты найдёшь подходящий именно тебе"
    )

    folder = "images/casual"

    media = []

    for image_name in os.listdir(folder):

        image_path = f"{folder}/{image_name}"

        photo = FSInputFile(image_path)

        media.append(
            InputMediaPhoto(media=photo)
        )

    await message.answer_media_group(media)


# Классика
@dp.message(F.text == "классика")
async def classic_style(message: Message):

    await message.answer(
        "вот тебе несколько образов💅\n"
        "надеюсь, ты найдёшь подходящий именно тебе"
    )

    folder = "images/classic"

    media = []

    for image_name in os.listdir(folder):

        image_path = f"{folder}/{image_name}"

        photo = FSInputFile(image_path)

        media.append(
            InputMediaPhoto(media=photo)
        )

    await message.answer_media_group(media)

# Sport Chic
@dp.message(F.text == "sports chic")
async def sport_chic_style(message: Message):

    await message.answer(
        "вот тебе несколько образов💅\n"
        "надеюсь, ты найдёшь подходящий именно тебе"
    )

    folder = "images/sports chic"

    media = []

    for image_name in os.listdir(folder):

        image_path = f"{folder}/{image_name}"

        photo = FSInputFile(image_path)

        media.append(
            InputMediaPhoto(media=photo)
        )

    await message.answer_media_group(media)


# Вечерний
@dp.message(F.text == "вечерний")
async def evening_style(message: Message):

    await message.answer(
        "вот тебе несколько образов💅\n"
        "надеюсь, ты найдёшь подходящий именно тебе"
    )

    folder = "images/evening"

    media = []

    for image_name in os.listdir(folder):

        image_path = f"{folder}/{image_name}"

        photo = FSInputFile(image_path)

        media.append(
            InputMediaPhoto(media=photo)
        )

    await message.answer_media_group(media)

# Кнопка "Назад"
@dp.message(F.text == "назад")
async def back_to_menu(message: Message):

    await message.answer(
        "ты в главном меню 💅",
        reply_markup=main_keyboard
    )
    
    # Кнопка "Подбор по цвету"
@dp.message(F.text == "подобрать по цвету")
async def choose_color(message: Message, state: FSMContext):

    await state.set_state(ColorSelection.first_color)

    await message.answer(
        "выбери первый цвет",
        reply_markup=colors_keyboard
    )

    # Выбор первого цвета
@dp.message(ColorSelection.first_color)
async def first_color(message: Message, state: FSMContext):

    await state.update_data(first_color=message.text)

    await state.set_state(ColorSelection.second_color)

    await message.answer(
        "выбери второй цвет"
    )
    # Выбор второго цвета
@dp.message(ColorSelection.second_color)
async def second_color(message: Message, state: FSMContext):

    await state.update_data(second_color=message.text)

    await state.set_state(ColorSelection.third_color)

    await message.answer(
        "выбери третий цвет"
    )
    # Выбор третьего цвета
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

    await state.clear()


# Запуск бота
async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(main())

