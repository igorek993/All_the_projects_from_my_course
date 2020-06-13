# -*- coding: utf-8 -*-

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.
import datetime
import re
import peewee

from WeatherMaker import WeatherMaker
from DatabaseUpdater import DatabaseUpdater
from ImageMaker import ImageMaker

db = peewee.SqliteDatabase('weather.db')
DATE_REG = re.compile(r"\d\d\.\d\d\.\d{4}")


class BaseTable(peewee.Model):
    class Meta:
        database = db


class Weather(BaseTable):
    date = peewee.CharField()
    max_temperature = peewee.CharField()
    min_temperature = peewee.CharField()
    weather_type = peewee.CharField()


db.create_tables([Weather])


class ControlPanel(DatabaseUpdater, WeatherMaker, ImageMaker):

    def __init__(self):
        super().__init__()
        self.data = self.get_data()
        self.initial_load(self.data, Weather)
        self.initial_date = "None"
        self.final_date = "None"
        self.dates_range = "None"

    def find_dates_range(self):
        self.dates_range = [self.initial_date + datetime.timedelta(days=x) for x in
                            range(0, (self.final_date - self.initial_date).days + 1)]

    def ask_date_range(self):
        while not (re.search(DATE_REG, str(self.initial_date)) and re.search(DATE_REG, str(self.final_date))):
            print(
                f"Please, choose the date range!\nDates available (should be added to the database first): "
                f"from {list(self.data.keys())[1].strftime('%d.%m.%Y')}"
                f" to {list(self.data.keys())[-1].strftime('%d.%m.%Y')}\nInitial date: (format D/M/Y, e.g. "
                f"{list(self.data.keys())[7].strftime('%d.%m.%Y')})")
            self.initial_date = input()
            print(f"Final date: (format D/M/Y, e.g. 30.06.2020)")
            self.final_date = input()
            if self.check_dates_range():
                break
        self.find_dates_range()

    def dates_str_to_daytime(self):
        day, month, year = str(self.initial_date).split(".")
        self.initial_date = datetime.date(year=int(year), day=int(day), month=int(month))
        day, month, year = str(self.final_date).split(".")
        self.final_date = datetime.date(year=int(year), day=int(day), month=int(month))

    def check_dates_range(self):
        self.dates_str_to_daytime()
        if self.initial_date < list(self.data.keys())[1] or self.final_date > list(self.data.keys())[-1]:
            print("These dates are not available!")
            self.reset_dates_range()
        else:
            return True

    def create_post_card(self):
        printed = False
        for day in Weather.select():
            year, month, c_day = day.date.split("-")
            date = datetime.date(int(year), int(month), int(c_day))
            date_to_print = f"{c_day}-{month}-{year}"
            if date in self.dates_range:
                printed = True
                self.make_postcard(date_to_print, day.min_temperature, day.max_temperature,
                                   day.weather_type.lower())
        if not printed:
            print("Dates are out of range or you haven't updated the database!\n")

    def add_date_range(self):
        self.ask_date_range()
        self.add_days(self.data, Weather, self.dates_range)
        self.reset_dates_range()

    def reset_dates_range(self):
        self.initial_date = "None"
        self.final_date = "None"
        self.dates_range = "None"

    def create_dates_range(self):
        self.ask_date_range()
        self.dates_range = self.get_dates_range(Weather, self.dates_range)

    def print_weather_forecast(self):
        printed = False
        for day in Weather.select():
            year, month, c_day = day.date.split("-")
            date = datetime.date(int(year), int(month), int(c_day))
            if date in self.dates_range:
                printed = True
                print(
                    f"_____________________\nDate: {date.strftime('%d.%m.%Y')}\nMin temp: {day.min_temperature}\nMax "
                    f"temp: {day.max_temperature}\nWeather type: {day.weather_type}\n_____________________")
        if not printed:
            print("Dates are out of range or you haven't updated the database!")

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
                    self.create_post_card()
                elif choice == "2":
                    self.print_weather_forecast()
                    self.reset_dates_range()


test = ControlPanel()
test.menu()
