# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_a_shape(start_point, angle, length):
        current_point = start_point
        max_angle = 360 + angle
        angle_step = 360 // n
        for angle in range(angle, max_angle, angle_step):
            current_point = sd.vector(current_point, angle, length)

    return draw_a_shape


draw_triangle = get_polygon(n=3)
draw_square = get_polygon(n=4)
draw_pentagon = get_polygon(n=5)
draw_pentagon(start_point=sd.get_point(200, 200), angle=13, length=150)

sd.pause()
