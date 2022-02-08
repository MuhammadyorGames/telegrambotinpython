import requests
import datetime
from config import open_weather_token


def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear":"Ясно ☀",
        "Clouds": "Облачно ⛅",
        "Rain": "Дождь 🌨",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B",
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

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
        length_of_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                f"Погода в городе: {city}\nТемпература: {cur_weather}C {wd}\n"
                f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind}\n"
                f"Восход солнца: {sunrise_ts}\nЗакат солнца: {sunset_ts}\nПродолжительность дня: {length_of_day}\n"
                f"Хорошего для!")

    except Exception as ex:
        print(ex)
        print("Error")


def main():
    city = input("Enter city name: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()

# api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}