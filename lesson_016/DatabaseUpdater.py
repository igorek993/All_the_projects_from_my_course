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

import datetime


class DatabaseUpdater:

    def add_days(self, data, db_object, dates_range):
        for key in data.keys():  # todo I do not really think I could do it because it's a preloaded dict
            # (so I do not have to ping yandex every x seconds) that sits
            # in the system from the very beginning and has all the data in it. The dates_range is just
            # like an indicator for the data that should be extracted from it. It does not actually gets it from
            # the server every time you ask for it. Please, correct me if I am wrong. I would like to be wrong here :)
            if dates_range[0] <= key <= dates_range[1]:
                self.update_weather_db(data, db_object, key)
        print("The database was updated!\n")

    def initial_load(self, data, db_object):
        counter = 0
        for key in data.keys():
            self.update_weather_db(data, db_object, key)
            counter += 1
            if counter == 5:
                break

    def update_weather_db(self, data, db_object, key):
        day = db_object.get_or_create(
            date=key,
            max_temperature=data[key]["max_temperature"],
            min_temperature=data[key]["min_temperature"],
            weather_type=data[key]["weather_type"]
        )

    def get_dates_range(self, db_object, dates_range):
        dates_to_return = list()
        for date in db_object.select():
            year, month, day = date.date.split("-")
            day = datetime.date(int(year), int(month), int(day))
            if day in dates_range:
                dates_to_return.append(day)
        return dates_range
