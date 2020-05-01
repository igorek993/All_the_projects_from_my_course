# -*- coding: utf-8 -*-
import os

from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

#
# def make_ticket(fio, from_, to, date):
#     font_path = os.path.join("python_snippets\\fonts", "OpenSans-Regular.ttf")
#     ticket = Image.open('images/ticket_template.png')
#     font = ImageFont.truetype(font_path, size=16)
#     draw = ImageDraw.Draw(ticket)
#
#     draw.text((45, 117), fio, font=font, fill=ImageColor.colormap['black'])
#     draw.text((45, 187), from_, font=font, fill=ImageColor.colormap['black'])
#     draw.text((45, 253), to, font=font, fill=ImageColor.colormap['black'])
#     draw.text((285, 253), date, font=font, fill=ImageColor.colormap['black'])
#
#     ticket.save('probe.png')
#
#
# if __name__ == "__main__":
#     make_ticket('Igor Zhukov', "Earth", "Moon", "09.12")
#


# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


parser = argparse.ArgumentParser(description="Ticket filler")
parser.add_argument("-fio", "--name_surname", required=True)
parser.add_argument("-from_", "--country_of_origin", required=True)
parser.add_argument("-t", "--destination", required=True)
parser.add_argument("-d", "--date", required=True)
parser.add_argument("-p", "--path", help='save to')
args = parser.parse_args()


# TODO Опреледения функций должны идти до основного кода
def make_ticket(fio, from_, to, date, path=None):
    font_path = os.path.join("python_snippets\\fonts", "OpenSans-Regular.ttf")
    ticket = Image.open('images/ticket_template.png')
    # TODO Все ресурсы (названия, пути к ним) должны быть в виде констант
    font = ImageFont.truetype(font_path, size=16)
    draw = ImageDraw.Draw(ticket)

    draw.text((45, 117), fio, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 187), from_, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 253), to, font=font, fill=ImageColor.colormap['black'])
    draw.text((285, 253), date, font=font, fill=ImageColor.colormap['black'])
    # TODO чтобы не дублировать код: создайте структуру данных с координатами текста и самим текстом (переменными) и
    #  в цикле итерируя по ней рисуйте текст
    ticket.save(path) if path else ticket.save('probe.png')  # TODO Аналогично


if __name__ == "__main__":
    make_ticket(args.name_surname, args.country_of_origin, args.destination, args.date, args.path)
