# -*- coding: utf-8 -*-
import datetime
import re
from collections import defaultdict

import bs4
import cv2
import requests
from PIL import Image, ImageDraw, ImageFont

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

from cv2.cv2 import FONT_HERSHEY_PLAIN

daytime_rg = re.compile(r"\d{4}-\d{2}-\d{2}")
temperature_rg = re.compile(r"\>[-+]\d{1,2}")
YANDEX_URL = "https://yandex.com/weather/21265?via=srp"


class WeatherMaker:

    def __init__(self):
        self.html = requests.get(YANDEX_URL).text
        self.soup = bs4.BeautifulSoup(self.html, 'html.parser')
        self.temperature_div = self.soup.find_all("div", class_="forecast-briefly__day")
        self.weather_type = self.soup.find_all("div", class_="forecast-briefly__condition")
        self.data = defaultdict(dict)

    def get_datetime(self):
        daytime = self.soup.find_all('time')
        for date in daytime:
            just_date = re.search(daytime_rg, str(date))
            current_date = datetime.datetime.strptime(just_date.group(), '%Y-%m-%d')
            self.data[current_date.date()].update({})

    def get_temperature(self):
        for temp, day, weather_type in zip(self.temperature_div, self.data, self.weather_type):
            high_low = re.findall(temperature_rg, str(temp))
            self.data[day].update({"max_temperature": high_low[0][1:], "min_temperature": high_low[1][1:],
                                   "weather_type": weather_type.string})

    def get_data(self):
        self.get_datetime()
        self.get_temperature()
        return self.data
