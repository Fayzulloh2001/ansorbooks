import  sqlite3
from aiogram.types import Message, CallbackQuery
from keyboards.default.key import menu
from keyboards.default.contac import inli
from data.config import ADMINS
from loader import dp, db, bot


@dp.callback_query_handler(text="tekshir")
async def contac(call: CallbackQuery):
    await call.message.answer("iltimos kontaktizni kiriting", reply_markup=inli )
    await call.answer(cache_time=10)
   
 

@dp.message_handler(content_types="contact")  
async def contact_message(message: Message):
    contact = message.contact.phone_number
     
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                   name=name,
                   contact=contact,
                   natijam=1)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)
    
    await message.answer(f"Kantaktingiz qabul qilindi:", reply_markup=menu)
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} royxatdan otdi: {count} foydalanuvchi boldi {contact}"
    await bot.send_message(chat_id=ADMINS[0], text=msg)
    return contact

