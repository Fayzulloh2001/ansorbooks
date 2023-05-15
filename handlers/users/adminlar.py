from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/barchasi", user_id=ADMINS)
async def get_allusers(message: types.Message):
    users = db.select_all_users()
    for use in users:
        ball = use[1]
        name = use[2]
        tel = use[4]
        await message.answer(f"<b>{ball}-ball</b>, <b>Ism:</b> {name}, <b>tel:</b>{tel}")
    
    