# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# - треугольник

start_point = sd.get_point(150, 150)


def triangle(point, angle, length):
    for _ in range(3):
        v1 = sd.get_vector(point, angle, length, 3)
        v1.draw()
        point = v1.end_point
        angle = angle + 120


# - квадрат

def square(point, angle, length):
    for _ in range(4):
        v1 = sd.get_vector(point, angle, length, 3)
        v1.draw()
        point = v1.end_point
        angle = angle + 90


# - пятиугольник

def pentagon(point, angle, length):
    for _ in range(5):
        v1 = sd.get_vector(point, angle, length, 3)
        v1.draw()
        point = v1.end_point
        angle = angle + 72


# - шестиугольник

def hexagon(point, angle, length):
    for _ in range(6):
        v1 = sd.get_vector(point, angle, length, 3)
        v1.draw()
        point = v1.end_point
        angle = angle + 60


# зачет первой части

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

def draw_a_shape(start_point, angle, length, number_of_sides):
    current_point = start_point
    for angle in range((360 // number_of_sides), (360 + (360 // number_of_sides)), 360 // number_of_sides):
        current_vector = sd.get_vector(current_point, angle, length, 3)
        sd.vector(current_point, angle, length)
        current_point = current_vector.end_point


def triangle_2(point, angle, length):
    draw_a_shape(point, angle, length, 3)


def square_2(point, angle, length):
    draw_a_shape(point, angle, length, 4)


def pentagon_2(point, angle, length):
    draw_a_shape(point, angle, length, 5)


def hexagon_2(point, angle, length):
    draw_a_shape(point, angle, length, 6)


#triangle_2(start_point, 0, 100)
#square_2(start_point, 0, 100)
#pentagon_2(start_point, 0, 100)
hexagon_2(start_point, 0, 100)

sd.pause()
