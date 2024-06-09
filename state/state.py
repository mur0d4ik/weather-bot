from aiogram.fsm.state import StatesGroup, State

class weatherStateCurrent(StatesGroup):
    location = State()

class weatherStateForecast(StatesGroup):
    day = State()
    location = State()