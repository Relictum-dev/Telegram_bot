from aiogram import types
from creation import dp, Doctor
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text


from keyboards.general_kb import spec_kb

@dp.message_handler(commands=['start'])
async def start_message(message : types.Message):
    await message.answer('Доброго времени суток!' '\n' '\n'
    'Прежде чем мы начнём, прошу авторизироваться или пройти минутную регистрацию' '\n' '\n'
    'С уважением - Профессор Ботвинк', reply_markup=spec_kb)


@dp.message_handler(Text(equals='Регистрация'))
async def register_user(message : types.Message):
    await message.answer('Введите электронную почту')


@dp.message_handler(Text(equals='Вход'))
async def enter_user(message: types.Message):
    await message.answer('Введите логин')


def register_general_handlers (dp : Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(register_user, Text(equals='Регистрация'))
    dp.register_message_handler(enter_user, Text(equals='Вход'))