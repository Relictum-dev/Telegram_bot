from aiogram import types
from creation import dp, Doctor
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text


from keyboards.general_kb import spec_kb, reg_kb, autoriz_kb
from connection_base import db_start, create_profile, edit_profile

async def on_start(_):
    await db_start()

@dp.message_handler(commands=['start'])
async def start_message(message : types.Message):
    
    await message.answer('Доброго времени суток!' '\n' '\n'
    'Прежде чем мы начнём, прошу авторизироваться или пройти минутную регистрацию' '\n' '\n'
    'С уважением - Профессор Ботвинк', reply_markup=spec_kb)

    await create_profile(user_id = message.from_user.id)



@dp.message_handler(Text(equals='Регистрация'))
async def register_user(message : types.Message):
    await message.answer('Введите электронную почту', reply_markup = reg_kb)



@dp.message_handler(Text(equals='Вход'))
async def enter_user(message: types.Message):
    await message.answer('Введите логин', reply_markup= autoriz_kb)


@dp.message_handler(Text(equals='Отменить регистрацию'))
async def back_registration (message: types.Message):
    await message.answer('Возвращаю к окну авторизации', reply_markup= spec_kb)


@dp.message_handler(Text(equals='Отменить авторизацию'))
async def back_autorization (message: types.Message):
    await message.answer('Возвращаю к окну авторизации', reply_markup= spec_kb)


def register_general_handlers (dp : Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(register_user, Text(equals='Регистрация'))
    dp.register_message_handler(back_registration, Text(equals='Отменить регистрацию'))
    dp.register_message_handler(back_autorization, Text(equals='Отменить авторизацию'))
    dp.register_message_handler(enter_user, Text(equals='Вход'))
