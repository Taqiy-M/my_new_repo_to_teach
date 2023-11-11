import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot_loyiha.database_kodlari import get_all_category_buttons
from bot_loyiha.statelarim import Holatlarim, AdminUchun

API_TOKEN = "6430667938:AAFQ7mdyI-SLpcnMhI8kxUpLOnG3x0EoBjk"
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def hello(msg: types.Message):
    await Holatlarim.kontaktState.set()
    keyboard = KeyboardButton("Kontakt ulashish", request_contact=True)
    await msg.answer("Kontaktingizni ulashing",
                     reply_markup=
                     ReplyKeyboardMarkup(resize_keyboard=True).add(keyboard))



@dp.message_handler(state=Holatlarim.kontaktState, content_types=['contact'])
async def kkk(msg: types.Message, state: FSMContext):
    keyboard = KeyboardButton("Lokatsiya yuborish", request_location=True)
    await msg.answer("Kontakt muvaffaqiyatli qo'shildi!! ✅", reply_markup=
                     ReplyKeyboardMarkup(resize_keyboard=True).add(keyboard))
    await Holatlarim.locationState.set()


@dp.message_handler(state=Holatlarim.locationState, content_types=['location'])
async def kkk(msg: types.Message, state: FSMContext):
    mrkp = ReplyKeyboardMarkup(resize_keyboard=True)
    mrkp.add(KeyboardButton("Menu"))
    mrkp.add(KeyboardButton("Sozlamalar"), KeyboardButton("Biz haqimizda"))
    mrkp.add(KeyboardButton("Tarix"))
    await msg.answer("Lokatiya muvaffaqiyatli qo'shildi!! ✅", reply_markup=mrkp)
    await Holatlarim.mainState.set()


@dp.message_handler(state=Holatlarim.mainState, text="Menu")
async def menu(msg: types.Message, state: FSMContext):
    await msg.answer("Nimadan boshlaymiz..", reply_markup=get_all_category_buttons())
    await Holatlarim.menuState.set()


@dp.message_handler(state="*", commands=['admin'])
async def kkk(msg: types.Message):
    await msg.answer("Yangi kategoriya nomi: ")
    await AdminUchun.nom.set()


@dp.message_handler(state=AdminUchun.nom)
async def kkk(msg: types.Message, state: FSMContext):
    await msg.answer("Yangi kategoriya nomi qabul qilindi!!! Endi rasm linkini yuboring.")
    await state.update_data({"nom": msg.text})
    await AdminUchun.rasm.set()


@dp.message_handler(state=AdminUchun.rasm)
async def kkk(msg: types.Message, state: FSMContext):
    await msg.answer("Yangi rasmi qabul qilindi!! Endi description yozing")
    await state.update_data({"rasm": msg.text})
    await AdminUchun.descr.set()


@dp.message_handler(state=AdminUchun.descr)
async def kkk(msg: types.Message, state: FSMContext):
    await msg.answer("Description qabul qilindi!! Yangi malumot qo'shildi!!!!")
    await state.update_data({"descr": msg.text})


    data = await state.get_data()

    query = f"""INSERT INTO Category (name, rasm, descr) VALUES ("{str(data["nom"])}", "{str(data["rasm"])}", "{str(data["descr"])}");"""
    kursor.execute(query)
    con.commit()
    await state.finish()

if __name__ == '__main__':
    con = sqlite3.connect("bazam.db")
    kursor = con.cursor()
    executor.start_polling(dp, skip_updates=True)





