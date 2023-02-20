from aiogram import types
from aiogram import Dispatcher
from creation import dp, Doctor


@dp.message_handler(commands=['start'])
async def start_message(message : types.Message):
    await message.answer('Привет')






def register_client_handlers (dp : Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])





