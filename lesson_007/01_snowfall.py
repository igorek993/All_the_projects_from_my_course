# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, number):
        self.number = number
        self.x = [sd.random_number(0, sd.resolution[0])]
        self.y = [sd.random_number(sd.resolution[1], sd.resolution[1] * 2)]
        self.flake_length = [sd.random_number(20, 50)]

    def clear_previous_picture(self):
        sd.start_drawing()
        for x, y, length in zip(self.x, self.y, self.flake_length):
            sd.snowflake(sd.get_point(x, y), length, color=sd.background_color)

    def move(self):
        self.x[0] += sd.random_number(-15, 15)
        self.y[0] -= sd.random_number(4, 30)

    def draw(self):
        for x, y, length in zip(self.x, self.y, self.flake_length):
            sd.snowflake(sd.get_point(x, y), length, color=sd.COLOR_WHITE)
        sd.finish_drawing()

    def can_fall(self):
        if self.y[0] <= self.flake_length[0]:
            return True


#
# flake = Snowflake(1)
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

def get_flakes(count):
    flakes = []
    for number in range(count):
        flakes.append(Snowflake(number=number))
    return flakes


def get_fallen_flakes():
    global flakes
    count = 0
    for flake in flakes:
        if flake.y[0] <= 0:
            count += 1
    return count


def append_flakes(count):
    global flakes
    for number in range(count):
        flakes.append(Snowflake(number=number))


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=20)  # создать список снежинок

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
