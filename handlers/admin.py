from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from create_bot import bot
from data_base import sqlite_db
from keyboards import admin_kb

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    url = State()
    name = State()
    des = State()

# @dp.message_handler(commands=['moderator'],is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'What do you want? :)', reply_markup=admin_kb.button_case_admin)
    await message.delete()

# @dp.message_handler(commands='load', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Load a photo')

# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Load Url to APK")

# @dp.message_handler(state=FSMAdmin.url)
async def load_apk(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['url'] = message.text
        await FSMAdmin.next()
        await message.reply("Type a name")

# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Type a description')

# @dp.message_handler(state=FSMAdmin.des)
async def load_des(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['des'] = message.text

        await sqlite_db.sql_add_command(state)
        await state.finish()

# @dp.message_handler(state="*", commands='cancel')
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state=FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')

def admin_handler_register(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['load'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_apk, state=FSMAdmin.url)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_des, state=FSMAdmin.des)
    dp.register_message_handler(cancel_handler, state="*", commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)