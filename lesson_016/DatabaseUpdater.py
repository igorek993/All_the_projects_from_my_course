# -*- coding: utf-8 -*-


# Добавить класс DatabaseUpdater с методами:
#   Сохраняющим прогнозы в базу данных (использовать peewee)
#   Получающим данные из базы данных за указанный диапазон дат.


# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database


import sqlite3
import peewee
from WeatherMaker import WeatherMaker

db = peewee.SqliteDatabase('weather.db')

weather = WeatherMaker()


class BaseTable(peewee.Model):
    class Meta:
        database = db


class Weather(BaseTable):
    date = peewee.CharField()
    max_temperature = peewee.CharField()
    min_temperature = peewee.CharField()
    weather_type = peewee.CharField()


db.create_tables([Weather])


class DatabaseUpdater:

    def save_forecast(self, data):
        for key in data.keys():
            day = Weather.create(
                date=key,
                max_temperature=data[key]["max_temperature"],
                min_temperature=data[key]["min_temperature"],
                weather_type=data[key]["weather_type"]
            )


test = DatabaseUpdater()
test.save_forecast(data=weather.get_data())
