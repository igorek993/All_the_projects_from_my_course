# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(300, 300)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def buble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=color)


# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    buble(point=point, step=5, color=(255, 127, 0))

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        buble(point=point, step=5, color=(255, 127, 0))

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(1, 101, 1):
    point = sd.random_point()
    step = random.randint(2, 10)
    colour_1 = random.randint(0, 255)
    colour_2 = random.randint(0, 255)
    colour_3 = random.randint(0, 255)
    buble(point=point, step=step, color=(colour_1, colour_2, colour_3))

sd.pause()
