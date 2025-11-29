from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    get_admin_message = State()