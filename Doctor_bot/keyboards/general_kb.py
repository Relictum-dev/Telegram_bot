from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# Клавиатура 1 (Стартовая клавиатура)
button_1 = KeyboardButton(text='Вход')
button_2 = KeyboardButton(text='Регистрация')
spec_kb = ReplyKeyboardMarkup()
spec_kb.add(button_1, button_2)


# Клавиатура 2 (Отмена регистрации)
btn_1 = KeyboardButton (text='Отменить регистрацию')

reg_kb = ReplyKeyboardMarkup()
reg_kb.add(btn_1)

# Клавиатура 3 (Отмена авторизации)
back_btn = KeyboardButton (text='Отменить авторизацию')

autoriz_kb = ReplyKeyboardMarkup()
autoriz_kb.add(back_btn)