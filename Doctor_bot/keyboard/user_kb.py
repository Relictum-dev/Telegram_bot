from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton


# Cоздание клавиатуры регистрации и входа
button_1 = KeyboardButton(text='Войти как пользователь')
welcome_kb = ReplyKeyboardMarkup()
welcome_kb.add (button_1)

# Создание клавиатуры пользователя
btn_1 = KeyboardButton(text='🌦 Погода')
btn_2 = KeyboardButton(text='🎲 Рандомайзер')

user_kb = ReplyKeyboardMarkup()
user_kb.add (btn_1,btn_2)

#создание inline клавиатуры
inline_btn_1 = InlineKeyboardButton('Да', callback_data='btn_yes')
inline_btn_2 = InlineKeyboardButton('Нет', callback_data='btn_no')
rules_kb = InlineKeyboardMarkup().add(inline_btn_1,inline_btn_2)


# Создание удаления клавиатуры

delete_kb =ReplyKeyboardRemove()
