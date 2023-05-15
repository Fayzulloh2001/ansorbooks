import sqlite3
from aiogram.dispatcher.filters import Command, Text
from keyboards.default.natija import natija
from aiogram import types
from keyboards.inline.test import tests, test1, test2, test3, test4, test5 ,test6, test7, test8, test9, test10, test11, test12,test13, test14,test15, test16, test17, test18, test19, test20
from aiogram.types import Message
import logging
from loader import dp,db, bot

@dp.message_handler(text="📝 Testni boshlash")
async def natijalar(message: Message):
    await bot.send_message(message.chat.id, "Testni boshlaymizmi?", reply_markup=natija)
    await bot.send_message(message.chat.id, " 1️⃣ Bizga yaqindan hamrohlik qiling; \n2️⃣ O`yinimiz bo`yicha 20 ta savolga javob toping; \n3️⃣ Sizga bu savollarga javob berish uchun 10daqiqa vaqt beriladi; \n Testga tayyormisiz ❗️❗️❗️ ", reply_markup=tests)
    
num_of_questions = 2



# Birinchi savolini yuborish
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('test_start'))
async def start_test_callback(callback_query: types.CallbackQuery):
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = 0            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 

#Javobni yuborish
       
       await bot.send_message(callback_query.from_user.id,f"1-savol \n Abdulloh Yorqinning otasi qanday fan o'qituvchisi edi?  \n javobingizni belgilang:", reply_markup=test1)

       await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
# Birinchi savolini tekshirish
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('test_answer_1'))
async def check_test_answer_1(callback_query: types.CallbackQuery):
    if callback_query.data == 'test_answer_1_2':
       users_id=callback_query.from_user.id
       ball = 1
       db.update_user_natijam(id=users_id,
                       natijam=ball)
       
    
# Ikkinchi savol

    
    await bot.send_message(callback_query.from_user.id,f"2-savol \n Shafiqaning turmush o'rtog'i bo'lgan Fotih Karimning asl yurti qaerda edi?  \n javobingizni belgilang:", reply_markup=test2)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
# Testning ikkinchi savolini tekshirish
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_2"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_2_1":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new)  
    

# Uchinchi savol   

    
    await bot.send_message(callback_query.from_user.id,f"3-savol \n -Hato qilish Odam atodan meros, Shafiqa. Tavba qilish ham uning sunnati. Robbisining qoshiga siniq qalb ila borish beayblik davosi ila borishdan ko'ra yahshiroqdir, inshaalloh... \n Bu so'zlarni Shafiqaga kim aytgan edi?  \n javobingizni belgilang:", reply_markup=test3)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
# uchinchi savolni tekshirish

@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_3"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_3_3":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 

    await bot.send_message(callback_query.from_user.id,f"4-savol \n Abdulloh Yorqinning kasbi nima edi?  \n javobingizni belgilang:", reply_markup=test4)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   

@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_4"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_4_2":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"5-savol \n Shafiqa otasining uyida asosan qanday kitoblar o'qishar edi?    \n javobingizni belgilang:", reply_markup=test5)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_5"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_5_2":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"6-savol \n Abdulloh Yorqinning bobosini ismi nima bo‘lgan?    \n javobingizni belgilang:", reply_markup=test6)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   

@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_6"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_6_2":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"7-savol \n Fotih Karimning ikkinchi ayolini ismi nima edi?  \n javobingizni belgilang:", reply_markup=test7)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   

                
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_7"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_7_1":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"8-savol \n  'Urvatul vusqo' kemasi jami necha kishini o‘ziga sig‘diradi? \n javobingizni belgilang:", reply_markup=test8)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   

@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_8"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_8_3":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"9-savol \n Mubinaning avvalgi ismi nima bo‘lgan? \n javobingizni belgilang:", reply_markup=test9)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_9"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_9_1":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"10-savol \n Anjelina qaysi shaharga borganida Bobur masjidini buzib tashlanganini ko‘rdi?  \n javobingizni belgilang:", reply_markup=test10)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   

@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_a"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_a_3":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"11-savol \n   Anjelinaning ilk ishi qayerda boshlandi?  \n javobingizni belgilang:", reply_markup=test11)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   
                                
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_b"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_b_2":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"12-savol \n Roziya Muhsin Shafiqa hushidan ketganda qaysi kasal boshlanayotganini aytdi? \n javobingizni belgilang:", reply_markup=test12)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   
                    
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_c"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_c_1":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"13-savol \n Anjelinaga mahalliy mutaxassislardan kim biriktirilgan? \n javobingizni belgilang:", reply_markup=test13)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   
                   
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_d"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_d_3":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"14-savol \n  Umarning otasi, Zaynabning erini ismi nima edi? \n javobingizni belgilang:", reply_markup=test14)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   

@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_e"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_e_1":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"15-savol \n Hikoyada kelishicha Bobilga qaysi farishtalar tushib, sehr qilishni o‘rgatib ketishadi? \n javobingizni belgilang:", reply_markup=test15)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_f"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_f_2":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"16-savol \n Abdullohbey Tublibek bilan bo‘lgan suhbatda qog‘ozga yozish asnosida qaysi suraning oyatlarini o‘qidi? \n javobingizni belgilang:", reply_markup=test16)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_g"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_g_3":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"17-savol \n Shayx Qosimnikiga sovchilikka kim bordi? \n javobingizni belgilang:", reply_markup=test17)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_h"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_h_3":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"18-savol \n Xo‘ja Ali nechanchi farzand edi? \n javobingizni belgilang:", reply_markup=test18)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)   
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_i"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_i_1":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"19-savol \n Humayroning erining ismi nima edi? \n javobingizni belgilang:", reply_markup=test19)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)  
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_j"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_j_1":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new) 
    
    await bot.send_message(callback_query.from_user.id,f"20-savol \n Rabindranat Thakurga qarindoshligi bilan maqtangan kim edi? \n javobingizni belgilang:", reply_markup=test20)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)  
@dp.callback_query_handler(lambda c: c.data and c.data.startswith("test_answer_k"))
async def check_test_answer_2(callback_query: types.CallbackQuery):
    if callback_query.data == "test_answer_k_2":
       users_id=callback_query.from_user.id
       userlar = db.select_all_users()

       for user in userlar:
           if users_id == user[0]:
              balls = int(user[1])
              ball_new = balls + 1            
              db.update_user_natijam(id=users_id,
                       natijam=ball_new)
    
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id) 
    