from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

inli = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='contact', request_contact=True ),
        ],
    ],
    resize_keyboard=True
)