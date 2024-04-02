from aiogram.utils.keyboard import ReplyKeyboardBuilder

def location_btn():
    
    builder = ReplyKeyboardBuilder()
    
    builder.button(text='📍', request_location=True)
    
    return builder