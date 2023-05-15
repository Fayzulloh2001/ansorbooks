from aiogram.dispatcher.filters import Command, Text
from keyboards.default.key import menu
from aiogram.types import Message

import logging


from loader import dp,db
@dp.message_handler(text="Ortga")
async def menyubot(message: Message):
      await message.answer(f"Ortga qaytish", reply_markup=menu)
# Echo bot
@dp.message_handler(text="🧮 Natijam")
async def menyubot(message: Message):
    
    ismi = message.from_user.full_name
    idlar = int(message.from_user.id)
    userlar = db.select_all_users()

    for user in userlar:
       
        if idlar == user[0]:
           
           BALL = user[1]
            
           

           
    await message.answer(f"{BALL} ta to`g`ri" )
@dp.message_handler(text="📊 Reyting natijalar")
async def reyting(message: Message):
       userlar = db.select_all_users()
       birinchi = []
       ikkinchi = []
       uchinchi = []
       for use in userlar:
            if use[1]==20:
                 ismi = use[2]
                 birinchi.append(ismi)
            elif use[1]==19:
                 ismi = use[2]
                 ikkinchi.append(ismi)
            elif use[1]==18:
                 ismi = use[2]
                 uchinchi.append(ismi)            
       await message.answer( f" 1 - o`rin {birinchi}, \n 2 - o`rin {ikkinchi}, \n 3 - o`rin {uchinchi}")         