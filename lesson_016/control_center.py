# -*- coding: utf-8 -*-

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.
import datetime

import peewee

from WeatherMaker import WeatherMaker
from DatabaseUpdater import DatabaseUpdater

db = peewee.SqliteDatabase('weather.db')


class BaseTable(peewee.Model):
    class Meta:
        database = db


class Weather(BaseTable):
    date = peewee.CharField()
    max_temperature = peewee.CharField()
    min_temperature = peewee.CharField()
    weather_type = peewee.CharField()


db.create_tables([Weather])


class ControlPanel(DatabaseUpdater, WeatherMaker):

    def __init__(self):
        super().__init__()
        self.data = self.get_data()
        self.initial_load(self.data, Weather)
        self.initial_date = None
        self.final_date = None
        self.dates_range = None

    def find_dates_range(self):
        day, month, year = str(self.initial_date).split(".")
        self.initial_date = datetime.date(year=int(year), day=int(day), month=int(month))
        day, month, year = str(self.final_date).split(".")
        self.final_date = datetime.date(year=int(year), day=int(day), month=int(month))
        self.dates_range = [self.initial_date + datetime.timedelta(days=x) for x in
                            range(0, (self.final_date - self.initial_date).days + 1)]

    def ask_dete_range(self):
        print(f"Please, choose the date range!\n Initial date: (format D/M/Y, e.g. 06.06.2020)")
        self.initial_date = input()
        print(f"Final date: (format D/M/Y, e.g. 30.06.2020)")
        self.final_date = input()
        self.find_dates_range()

    def add_date_range(self):
        self.ask_dete_range()
        self.add_days(self.data, Weather, self.dates_range)
        self.reset_dates_range()

    def reset_dates_range(self):
        self.initial_date = None
        self.final_date = None
        self.dates_range = None

    def create_dates_range(self):
        self.ask_dete_range()
        self.dates_range = self.get_dates_range(Weather, self.dates_range)

    def print_weather_forecast(self):
        for day in Weather.select():
            year, month, c_day = day.date.split("-")
            date = datetime.date(int(year), int(month), int(c_day))
            if date in self.dates_range:
                print(f"_____________________\nDate: {day.date}\nMin temp: {day.min_temperature}\nMax temp: "
                      f"{day.max_temperature}\nWeather type: {day.weather_type}\n_____________________")

    def menu(self):
        while True:
            print(f"Options:\n1)Add weather forecast for a date range into the database\n"
                  f"2)Get a dates range from the database\n")
            choice = input()
            if choice == "1":
                self.add_date_range()
            elif choice == "2":
                self.create_dates_range()
                print(
                    f"Options:\n1)Create post-cards for this date range\n2)Print weather forecast for this date range")
                choice = input()
                if choice == "1":
                    pass
                elif choice == "2":
                    self.print_weather_forecast()
                    self.reset_dates_range()


test = ControlPanel()
test.menu()
