from aiogram.fsm.state import State, StatesGroup


class ColorSelection(StatesGroup):

    first_color = State()

    second_color = State()

    third_color = State()