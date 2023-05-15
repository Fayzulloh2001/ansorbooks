import sqlite3
from .adminlar import get_allusers
import logging
from aiogram import types
from data.config import CHANNEL, ADMINS
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.inlin import categoryMenu
from utils.misc.subscribt import check
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
   
    channels_format = str()
    for channel in CHANNEL:
         chat = await bot.get_chat(channel)
         invite_linke = await chat.export_invite_link()
         channels_format += f"👉 <a href='{invite_linke}'>{chat.title}</a> \n"
    await message.answer(f" Botdan foydalanish  uchun kanalga   azo boling \n👇👇👇👇👇👇👇👇👇👇", reply_markup=categoryMenu, disable_web_page_preview=True)
    

@dp.callback_query_handler(text='tekshir')
async def bot_tekshir(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNEL:
        status = await check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"✅ <b>{channel.title}</b> kanalga obuna bo`lgansiz \n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌ <b>{channel.title}</b> kanalga obuna bo`lgamagansiz \n{invite_link}")
    await call.message.answer(result, reply_markup=categoryMenu, disable_web_page_preview=True)
    await call.message.edit_reply_markup()