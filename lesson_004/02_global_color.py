# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
# вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом


# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def triangle(point, angle, length, color):
    for _ in range(3):
        v1 = sd.get_vector(point, angle, length, 3)
        v1.draw(color=color)
        point = v1.end_point
        angle = angle + 120


def square(point, angle, length, color):
    for _ in range(4):
        v1 = sd.get_vector(point, angle, length, 3)
        v1.draw(color=color)
        point = v1.end_point
        angle = angle + 90


def pentagon(point, angle, length, color):
    for _ in range(5):
        v1 = sd.get_vector(point, angle, length, 3)
        v1.draw(color=color)
        point = v1.end_point
        angle = angle + 72


def hexagon(point, angle, length, color):
    for _ in range(6):
        v1 = sd.get_vector(point, angle, length, 3)
        v1.draw(color=color)
        point = v1.end_point
        angle = angle + 60


def all_shapes(color):
    point_1 = sd.get_point(150, 50)
    point_2 = sd.get_point(150, 450)
    point_3 = sd.get_point(400, 50)
    point_4 = sd.get_point(400, 350)
    triangle(point_1, 0, 100, color)
    square(point_2, 0, 100, color)
    pentagon(point_3, 0, 100, color)
    hexagon(point_4, 0, 100, color)


colors = [
    {'name': 'red', 'code': sd.COLOR_RED},
    {'name': 'orange', 'code': sd.COLOR_ORANGE},
    {'name': 'yellow', 'code': sd.COLOR_YELLOW},
    {'name': 'green', 'code': sd.COLOR_GREEN},
    {'name': 'cyan', 'code': sd.COLOR_CYAN},
    {'name': 'blue', 'code': sd.COLOR_BLUE},
    {'name': 'purple', 'code': sd.COLOR_PURPLE},
]


def ask_for_a_color():
    number = 0
    for i in colors:
        print(number, i['name'])
        number += 1
        # TODO Примените enumerate в for вместо отдельного счётчика

    print('Please, select a color:')
    user_input = input()
    color = int(user_input)
    while color > len(colors) - 1:
        print('This color does not exist')
        print('Please, select a color:')
        user_input = input()
        color = int(user_input)
    else:
        all_shapes(colors[color]['code'])
        # TODo Согласно назначению функции "спросить цвет" и возвращать надо именно цвет, а вызвать функцию
        #  рисования фигуры надо в основном коде


ask_for_a_color()

sd.pause()
