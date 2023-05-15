from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📝 Testni boshlash'),

        ],
        [
           KeyboardButton(text="🧮 Natijam"),
           KeyboardButton(text = "📊 Reyting natijalar"),
           
        ],
    ],
    resize_keyboard=True
)