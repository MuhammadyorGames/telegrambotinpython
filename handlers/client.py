from aiogram import types, Dispatcher
from create_bot import bot
import requests, datetime
from keyboards.client_kb import kb_client, urlkb
from config import open_weather_token
from data_base import sqlite_db


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте введите название города 🏙', reply_markup=kb_client)
#     await bot.send_message(message.from_user.id, 'Здравствуйте чего вы хотите? 🙂', reply_markup=kb_client)

async def get_weather(message: types.Message):
    
        code_to_smile = {
            "Clear": "Ясно ☀",
            "Clouds": "Облачно ⛅",
            "Rain": "Дождь 🌧",
            "Drizzle": "Дождь 🌧",
            "Thunderstorm": "Гроза ⛈",
            "Snow": "Снег 🌨",
            "Mist": "Туман 🌫",
        }

        try:
            r = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={message.text.lower()}&appid={open_weather_token}&units=metric"
            )
            data = r.json()

            city = data["name"]
            cur_weather = data["main"]["temp"]

            weather_des = data["weather"][0]["main"]
            if weather_des in code_to_smile:
                wd = code_to_smile[weather_des]
            else:
                wd = "Сам посмотри что за погода я не знаю!"

            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]
            sunrise_ts = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset_ts = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
            length_of_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
                data["sys"]["sunrise"])

            await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                  f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
                  f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                  f"Восход солнца: {sunrise_ts}\nЗакат солнца: {sunset_ts}\nПродолжительность дня: {length_of_day}\n"
                  f"***Хорошего для!***")

        except:
            await message.reply("❌ Error ❌")

def client_handler_register(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    # dp.register_message_handler(apps, commands=['apps'])
    dp.register_message_handler(get_weather)
