# -*- coding: utf-8 -*-
import datetime
import re
from collections import defaultdict

import bs4
import cv2
import requests
from PIL import Image, ImageDraw, ImageFont

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
CLOUD_IMG = "C:\\Users\igorek\PycharmProjects\python_base\lesson_016\python_snippets\external_data\weather_img\clouds.png"
BLANK_SHEET = "C:\\Users\igorek\PycharmProjects\python_base\lesson_016\python_snippets\external_data\probe.jpg"
POST_CARDS_FOLDER = "C:\\Users\igorek\PycharmProjects\python_base\lesson_016\post_cards\\"
# TODO У каждого участника проекта свои собственные уникальные абсолютные пути к папке проекта, поэтому надо
#  использовать только относительные пути внутри проекта


class ImageMaker:

    def __init__(self):
        self.current_img = None
        self.font = ImageFont.truetype("Samble_Tracie_Bold.ttf", 20)
        # todo файл шрифта тоже должен быть "константой"
        # self.weather_data = weather_data

    def viewImage(self, image):
        cv2.namedWindow("window", cv2.WINDOW_NORMAL)
        cv2.imshow("window", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def draw_sunny_gradient(self):
        img = cv2.imread(BLANK_SHEET)
        for x in range(256):
            cv2.line(img, (0, x), (512, x), (x, 255, 255), 1)
        self.current_img = img

    def draw_rainy_gradient(self):
        img = cv2.imread(BLANK_SHEET)
        for x in range(256):
            cv2.line(img, (0, x), (512, x), (255, x, x), 1)
        self.current_img = img

    def draw_snow_gradient(self):
        img = cv2.imread(BLANK_SHEET)
        for x in range(256):
            cv2.line(img, (0, x), (512, x), (255, 255, x), 1)
        self.current_img = img

    def draw_cloudy_gradient(self):
        img = cv2.imread(BLANK_SHEET)
        for x in range(256):
            cv2.line(img, (0, x), (512, x), (90 + x, 90 + x, 90 + x), 1)
        self.current_img = img

    def put_weather_picture(self, weather_type):
        x_offset = y_offset = 50
        if "clear" in weather_type:
            paste_img = cv2.imread(SUN_IMG)
        elif "cloudy" or "overcast" in weather_type:
            paste_img = cv2.imread(CLOUD_IMG)
        elif "rain" in weather_type:
            paste_img = cv2.imread(RAIN_IMG)
        elif "snow" in weather_type:
            paste_img = cv2.imread(SNOW_IMG)
        self.current_img[y_offset:y_offset + paste_img.shape[0], x_offset:x_offset + paste_img.shape[1]] = paste_img

    def no_white_bg(self):
        for x in range(50, 150):
            current_color = self.current_img[x, 0]
            for y in range(50, 150):
                compare = self.current_img[x, y] > (239, 239, 239)
                if compare.all():
                    self.current_img[x, y] = current_color

    def put_text(self, date, min_temp, max_temp, weather_type):
        prints = [date, min_temp, max_temp, weather_type]
        labels = ["Date: ", "Min temperature: ", "Min temperature: ", "Weather: "]
        y = 60
        for text, label in zip(prints, labels):
            self.current_img = cv2.putText(self.current_img, (label + text), (250, y), cv2.FONT_HERSHEY_TRIPLEX,
                                           0.5, (0, 191, 255))
            y += 30

    def draw_necessary_gradient(self, weather_type):
        if "clear" in weather_type:
            self.draw_sunny_gradient()
        elif "cloudy" in weather_type:
            self.draw_cloudy_gradient()
        elif "rain" in weather_type:
            self.draw_rainy_gradient()
        elif "snow" in weather_type:
            self.draw_snow_gradient()

    def make_postcard(self, date, min_temp, max_temp, weather_type):
        self.draw_necessary_gradient(weather_type)
        self.put_weather_picture(weather_type)
        self.no_white_bg()
        self.put_text(date, min_temp, max_temp, weather_type)
        cv2.imwrite(POST_CARDS_FOLDER+date+".jpg", self.current_img)
