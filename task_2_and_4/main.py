
import asyncio
import logging
import sys

import requests as requests
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from task_2_and_4.buttons.main import main_buutons
from task_2_and_4.buttons.start_buttons import start_butons, month_buttons, days_buttons
from aiogram.fsm.context import FSMContext
from bs4 import BeautifulSoup
from aiogram.fsm.state import State, StatesGroup

TOKEN = "6331298174:AAG-fC9A-Ci_8Bna8x9DppOI-Te1sS7tA5k"


dp = Dispatcher()

class Menu(StatesGroup):
    menu = State()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=main_buutons())

@dp.message(lambda msg: msg.text == 'Start ✅')
async def start_button(msg: Message):
    await msg.answer("Quydagilardan birontasini tanlang 👇🏿", reply_markup=start_butons())

@dp.message(lambda msg: msg.text == "Woman")
@dp.message(lambda msg: msg.text == "Men")
async def start_button(msg: Message):
    await msg.answer("Quydagilardan birontasini tanlang 👇🏿", reply_markup=month_buttons())


@dp.message(lambda msg: msg.text == "1-oy")
@dp.message(lambda msg: msg.text == "2-oy")
@dp.message(lambda msg: msg.text == "3-oy")
@dp.message(lambda msg: msg.text == "4-oy")
async def start_button(msg: Message):
    await msg.answer("Quydagilardan birontasini tanlang 👇🏿", reply_markup=days_buttons())


@dp.message(lambda msg: msg.text == 'Admin 👨🏻‍💻')
async def start_button(msg: Message):
    await msg.answer("https://t.me/sarvarbek_12")

@dp.message(lambda msg: msg.text == 'Filial 📍')
async def start_button(msg: Message):
    await msg.answer("Bu bolim hozircha ishlamaydi")
@dp.message(lambda msg: msg.text == '🔙 back')
async def start_button(msg: Message):
    await msg.answer("Quydagilardan birontasini tanlang 👇🏿", reply_markup=main_buutons())




async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


