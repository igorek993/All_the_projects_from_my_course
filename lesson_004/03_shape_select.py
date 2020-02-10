# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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


shapes_functions = {0: triangle, 1: square, 2: pentagon, 3: hexagon}
shapes = [': треугольник', ': квадрат', ': пятиугольник', ': шестиугольник']

print('what shape would you like to draw?')
for _ in range(0, len(shapes), 1):
    print(_, shapes[_])


def ask_for_a_shape():
    user_input = input()
    shape = int(user_input)
    if shape <= len(shapes):
        shapes_functions[shape](sd.get_point(250, 250), 0, 100, sd.COLOR_YELLOW)
    else:
        print('This shape does not exist, please try again')
        ask_for_a_shape()


ask_for_a_shape()
sd.pause()
