from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-usul.
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Azo bo`lish 1 kanal", url="https://t.me/shunchakiy_qiziqish1"),
       
    ],
    
    [
        InlineKeyboardButton(text="Tekshirish", callback_data="tekshir"),
    ],
])
