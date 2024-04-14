from aiogram.fsm.state import StatesGroup, State

class weatherState(StatesGroup):
    location = State()
