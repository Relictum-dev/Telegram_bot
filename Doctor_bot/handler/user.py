from aiogram import types
from create import dp, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard.user_kb import welcome_kb, delete_kb
from database import add_user_to_db


# Создаём класс для хранения стейтов
class Enter_data(StatesGroup):
    login = State()
    password = State() 
    note = State()

# Описание хендлера [/start]
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Доброго времени суток, {message.chat.first_name} \n' '\n'
    'Прежде чем мы начнём, прошу пройти авторизацию или минутную авторизацию' '\n' '\n'
    'С уважением - Профессор Ботвинк', reply_markup= welcome_kb)

    

###### Описание хендлеров входа #######



##### Описание хендлеров регистрации ######

# Первый хендлер регистрации 
# Объявление значения стейта = None
@dp.message_handler(Text(equals='Регистрация'), state=None)
async def registration(message: types.Message):
    await message.answer('Придумайте логин', reply_markup=delete_kb)
    await Enter_data.login.set()

# Второй хендлер регистрации
# Значение стейта = login
@dp.message_handler(state = Enter_data.login)
async def registration_1(message: types.Message, state= FSMContext):
    answer = message.text 
    if len(answer) <= 3:
        await message.answer('Логин должен быть длиннее 3-х символом')
        return registration_1
    elif len(answer) > 15:
        await message.answer ('Логин не должен превышать 15 символов')
        return registration_1
    else:
        async with state.proxy() as data:
            data['login'] = answer
        await message.answer('Придумайте пароль', reply_markup= delete_kb)
        await Enter_data.next()

# Третий хендлер регистрации
# Значение стейта = password
@dp.message_handler(state= Enter_data.password)
async def registration_2(message: types.Message, state: FSMContext):

    data = await state.get_data()
    login = data.get('login')
    password = message.text
    await message.answer('Регистрация прошла успешно!', reply_markup= welcome_kb)
    await add_user_to_db(user_id=message.from_user.id, login=login, password=password)

    # сбрасываем значение стейтов после всех манипуляций с данными
    await state.finish()



# Регистрация хендреров для передачи в файл starting
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands = ['start'])
    dp.register_message_handler(registration, Text(equals='Регистрация'))
    dp.register_message_handler(registration_1, state= Enter_data.login)
    dp.register_message_handler(registration_2, state= Enter_data.password)
