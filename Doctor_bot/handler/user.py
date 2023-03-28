from aiogram import types
from create import dp, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard.user_kb import welcome_kb, delete_kb, user_kb, rules_kb
from database import add_user_to_db
import database
from create import owm, mrg
from random import randint

# Стейт погоды
class In_weather(StatesGroup):
    city = State()


# Создаём класс для хранения стейтов
class Enter_data(StatesGroup):
    login = State()
    password = State()

class Examination(StatesGroup):
    user_login = State()
    user_password = State()

# Описание хендлера [/start]
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Доброго времени суток, {message.chat.first_name} \n' '\n'
    'Прежде чем мы начнём, прошу пройти авторизацию или минутную авторизацию' '\n' '\n'
    'С уважением - Профессор Ботвинк', reply_markup= welcome_kb)

    
###### Описание хендлеров входа #######

# Первый хендлер входа
@dp.message_handler(Text(equals='Вход'), state=None)
async def enter(message: types.Message):
    await message.answer('Введите логин', reply_markup=delete_kb)
    await Examination.user_login.set()
 
 # Второй хендлер входа
@dp.message_handler(state = Examination.user_login)
async def enter_1(message: types.Message, state = FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['login'] = answer
        await message.answer('Введите пароль', reply_markup= delete_kb)
        await Examination.next()


#Третий хендлер входа
@dp.message_handler(state= Examination.user_password)
async def enter_2(message: types.Message, state: FSMContext):

    data = await state.get_data()
    login = data.get('login')
    password = message.text

    if login == database.user_check_login(login) and password == database.user_check_password(password):
        await message.answer('Добро пожаловать в личный кабинет!')
    else:
        await message.answer('Ошибка! Проверьте введённые вами данные')


    await state.finish()

##### Описание хендлеров регистрации ######

# Первый хендлер регистрации 
# Объявление значения стейта = None
@dp.message_handler(Text(equals='Войти как пользователь'), state=None)
async def registration(message: types.Message):
    await message.answer('Введите логин', reply_markup=delete_kb)
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
        await message.answer('Введите пароль', reply_markup= delete_kb)
        await Enter_data.next()

# Третий хендлер регистрации
# Значение стейта = password
@dp.message_handler(state= Enter_data.password)
async def registration_2(message: types.Message, state: FSMContext):

    data = await state.get_data()
    login = data.get('login')
    password = message.text
    if not (await database.user_exists(message.from_user.id)):
        await add_user_to_db(user_id=message.from_user.id, login=login, password=password)
        await message.answer('Рады приветствовать вас в первый раз, ' + message.chat.first_name, reply_markup= user_kb)
    else:
        await message.answer('Здравствуйте, ' + message.chat.first_name, reply_markup=user_kb)

    # сбрасываем значение стейтов после всех манипуляций с данными
    await state.finish()


dp.message_handler(Text(equals= '🌦 Погода'), state= None)
async def weather(message: types.Message):
    await message.answer('Введите город')
    await In_weather.city.set()

@dp.message_handler(state = In_weather.city)
async def weather_print(message: types.Message, state = FSMContext):
    answer = message.text
    try:
        async with state.proxy() as data:
            data['city'] = answer
            observation = mrg.weather_at_place(answer)
            weather = observation.weather
            await message.answer('Погода в городе ' + answer + ':' '\n' '\n'
            '*---Погодные условия---*' '\n' '\n'
            'Температура воздуха: ' '\n' + str(weather.temperature('celsius')['temp']) + '°C' '\n' '\n'
            'Скорость ветра:' '\n' + str(weather.wind()['speed']) + ' м/с' '\n' '\n' 
            '*--------------------------*',
            parse_mode='Markdown')
            await state.finish()
    except:
        await message.answer('Указанный город не найден')

@dp.message_handler(Text(equals='🎲 Рандомайзер'))
async def randomizer(message: types.Message):
    random_number = randint(1,10)
    await message.answer('Ваше случайное число от 1 до 10:' '\n' + str(random_number))


# Регистрация хендреров для передачи в файл starting
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands = ['start'])
    dp.register_message_handler(registration, Text(equals='Регистрация'))
    dp.register_message_handler(registration_1, state= Enter_data.login)
    dp.register_message_handler(registration_2, state= Enter_data.password)
    dp.register_message_handler(enter, Text(equals='Вход'))
    dp.register_message_handler(weather, Text(equals= '🌦 Погода'))
    dp.register_message_handler(randomizer, Text(equals='🎲 Рандомайзер'))
