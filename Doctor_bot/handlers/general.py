from aiogram import types
from creation import dp, Doctor
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.general_kb import spec_kb, reg_kb, autoriz_kb
from connection_base import db_start, create_profile, edit_profile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

async def on_start(_):
    await db_start()

class Info(StatesGroup):
    
    login = State()
    password = State()
    note = State()

    
@dp.message_handler(commands=['start'])
async def start_message(message : types.Message):
    await message.answer('Доброго времени суток!' '\n' '\n'
    'Прежде чем мы начнём, прошу авторизироваться или пройти минутную регистрацию' '\n' '\n'
    'С уважением - Профессор Ботвинк', reply_markup=spec_kb)

@dp.message_handler(Text(equals='Вход'),state= None)
async def enter_user(message: types.Message):
    await Info.login.set()
    await message.answer('Введите логин')
# Ловим первый ответ пользователя
@dp.message_handler(content_types=['login'], state=Info.login)
async def load_login(message: types.Message, state: Info):
    async with state.proxy() as data:
        data['login'] = message.text
    await Info.next()
    await message.answer('Теперь введите пароль')

# Ловим второй ответ пользователя
@dp.message_handler(state=Info.password)
async def load_password(message: types.Message, state: Info):
    async with state.proxy() as data:
        data['password'] = message.text
    await Info.next()
    await message.answer('Введите заметку')

# Ловим третий ответ пользователя 
@dp.message_handler(state= Info.note)
async def load_note(message: types.Message, state: Info):
    async with state.proxy() as data:
        data['note'] = message.text
    await Info.last()
    await message.answer('Заметка создана ✅')




def register_general_handlers (dp : Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(enter_user, state= None)
    dp.register_message_handler(load_login, state= Info.login)
    dp.register_message_handler(load_password, state = Info.password)
    dp.register_message_handler(load_note, state= Info.note)
    #dp.register_message_handler(register_user, Text(equals='Регистрация'))
    #dp.register_message_handler(back_registration, Text(equals='Отменить регистрацию'))
    #dp.register_message_handler(back_autorization, Text(equals='Отменить авторизацию'))
