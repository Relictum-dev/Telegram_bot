from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# Клавиатура 1
button_1 = KeyboardButton(text='Регистрация')
button_2 = KeyboardButton(text='Вход')
spec_kb = ReplyKeyboardMarkup()
spec_kb.add(button_1, button_2)
