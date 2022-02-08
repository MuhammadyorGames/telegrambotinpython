from aiogram import types, Dispatcher
from create_bot import bot
import string,json

# @dp.message_handler()
async def filter(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('mat.json')))) != set():
        await message.reply('Маты запрещены!')
        await message.delete()


def other_handler_register(dp: Dispatcher):
    dp.register_message_handler(filter)
