from aiogram.fsm.state import State, StatesGroup

class SearchLang(StatesGroup):
    lang = State()
    
class WeatherS(StatesGroup):
    location = State()