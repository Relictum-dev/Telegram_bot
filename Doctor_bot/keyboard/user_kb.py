from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton


# Cоздание клавиатуры регистрации и входа

button_1 = KeyboardButton(text='Вход')
button_2 = KeyboardButton(text='Регистрация')

welcome_kb = ReplyKeyboardMarkup()
welcome_kb.add (button_1, button_2)


# Создание удаления клавиатуры

delete_kb =ReplyKeyboardRemove()
