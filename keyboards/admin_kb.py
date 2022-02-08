from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

button_load = KeyboardButton('/load')
button_delete = KeyboardButton('/delete')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load, button_delete)