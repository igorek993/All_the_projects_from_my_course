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


class WeatherMaker:

    def __init__(self):
        self.html = requests.get('https://yandex.com/weather/21265?via=srp').text
        self.soup = bs4.BeautifulSoup(self.html, 'html.parser')
        self.temperature_div = self.soup.find_all("div", class_="forecast-briefly__day")
        self.weather_type = self.soup.find_all("div", class_="forecast-briefly__condition")
        self.data = defaultdict(dict)

    def get_datetime(self):
        daytime = self.soup.find_all('time')
        for date in daytime:
            just_date = re.search(daytime_rg, str(date))
            current_date = datetime.datetime.strptime(just_date.group(), '%Y-%m-%d')
            self.data[str(current_date.date())].update({})

    def get_temperature(self):
        for temp, day, weather_type in zip(self.temperature_div, self.data, self.weather_type):
            high_low = re.findall(temperature_rg, str(temp))
            self.data[day].update({"max_temperature": high_low[0][1:], "min_temperature": high_low[1][1:],
                                   "weather_type": weather_type.string})

    def run(self):
        self.get_datetime()
        self.get_temperature()
        return self.data


test = WeatherMaker()

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

SUN_IMG = 'C:\\Users\igorek\PycharmProjects\python_base\lesson_016\python_snippets\external_data\weather_img\sun.jpg'
RAIN_IMG = "C:\\Users\igorek\PycharmProjects\python_base\lesson_016\python_snippets\external_data\weather_img\\rain.jpg"
SNOW_IMG = "C:\\Users\igorek\PycharmProjects\python_base\lesson_016\python_snippets\external_data\weather_img\snow.jpg"
CLOUD_IMG = "C:\\Users\igorek\PycharmProjects\python_base\lesson_016\python_snippets\external_data\weather_img\cloud.jpg"
BLANK_SHEET = "C:\\Users\igorek\PycharmProjects\python_base\lesson_016\python_snippets\external_data\probe.jpg"
POST_CARDS_FOLDER = "C:\\Users\igorek\PycharmProjects\python_base\lesson_016\post_cards\\"


class ImageMaker:

    def __init__(self, weather_data):
        self.current_img = None
        self.font = ImageFont.truetype("Samble_Tracie_Bold.ttf", 20)
        self.weather_data = weather_data

    def draw_sunny_gradient(self):
        img = Image.open(BLANK_SHEET)
        for x in range(512):
            for y in range(256):
                img.putpixel((x, y), (255, 255, y // 1))
        self.current_img = img

    def draw_rainy_gradient(self):
        img = Image.open(BLANK_SHEET)
        for x in range(512):
            for y in range(256):
                img.putpixel((x, y), (y, y, 255))
        self.current_img = img

    def draw_snow_gradient(self):
        img = Image.open(BLANK_SHEET)
        for x in range(512):
            for y in range(256):
                img.putpixel((x, y), (y + 50, y + 100, 221))
        self.current_img = img

    def draw_cloudy_gradient(self):
        img = Image.open(BLANK_SHEET)
        for x in range(512):
            for y in range(256):
                color = y
                if y < 80:
                    color = 255
                img.putpixel((x, y), (color, color, color))
        self.current_img = img

    def put_weather_picture(self, date):
        self.draw_sunny_gradient()
        paste_img = Image.open(SUN_IMG)
        self.current_img.paste(paste_img, (50, 50))
        self.put_text(date)

    def put_text(self, date):
        img_to_draw = ImageDraw.Draw(self.current_img)
        y = 30
        img_to_draw.text((300, y), date, fill=(1, 1, 1), font=self.font)
        for key in self.weather_data[date].keys():
            y += 30
            info = self.weather_data[date][key]
            img_to_draw.text((300, y), f"{key}: {info}", fill=(1, 1, 1), font=self.font)
        self.current_img.show()

    def make_postcard(self, date, temperature, weather_type):
        pass


test2 = ImageMaker(weather_data=test.run())
test2.put_weather_picture("2020-06-09")
