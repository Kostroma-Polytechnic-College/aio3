from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_kb_by_start() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Регистрация', 
                callback_data='user_registration')
        ]
    ])