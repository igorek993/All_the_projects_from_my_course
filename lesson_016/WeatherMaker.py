# -*- coding: utf-8 -*-
import datetime
import re
from collections import defaultdict
from pprint import pprint
from PIL import Image

import bs4
import requests

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}


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


# test = WeatherMaker()
# test.run()

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
RAIN_IMG = "C:\\Users\igorek\PycharmProjects\python_base\lesson_016\python_snippets\external_data\weather_img\rain.jpg"
SNOW_IMG = "C:\\Users\igorek\PycharmProjects\python_base\lesson_016\python_snippets\external_data\weather_img\snow.jpg"
CLOUD_IMG = "C:\\Users\igorek\PycharmProjects\python_base\lesson_016\python_snippets\external_data\weather_img\cloud.jpg"
BLANK_SHEET = "C:\\Users\igorek\PycharmProjects\python_base\lesson_016\python_snippets\external_data\probe.jpg"


class ImageMaker:

    # def __init__(self):
    # sunny_gradient = (255, 255, y // 1)
    # rainy_gradient = (y // 1, y // 1, 255))
    snow_gradient =

    def draw_gradient(self):
        im = Image.open(BLANK_SHEET)
        for x in range(512):
            for y in range(256):
                im.putpixel((x, y), (y // 1, y // 1, 255))
        im.show()


test2 = ImageMaker()
test2.draw_gradient()
