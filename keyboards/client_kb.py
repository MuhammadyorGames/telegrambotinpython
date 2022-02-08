from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

b2 = KeyboardButton('Приложения')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

urlkb = InlineKeyboardMarkup(row_width=1)
site = InlineKeyboardButton(text='Сайт', url='http://h94972as.beget.tech/')
csgoM = InlineKeyboardButton(text='CSGO mobile', url='http://h94972as.beget.tech/apk/csgo.apk')
PNStrike = InlineKeyboardButton(text='P:N Strike', url='http://h94972as.beget.tech/apk/PN-Strike.apk')
urlkb.add(site)
urlkb.row(csgoM, PNStrike)


# kb_client.add(b2)
