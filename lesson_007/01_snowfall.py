# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(0, sd.resolution[0])
        self.y = sd.random_number(sd.resolution[1], sd.resolution[1] * 2)
        self.length = sd.random_number(20, 50)

    def clear_previous_picture(self):
        sd.snowflake(sd.get_point(self.x, self.y), self.length, color=sd.background_color)

    def move(self):
        self.x += sd.random_number(-15, 15)
        self.y -= sd.random_number(4, 30)

    def draw(self):
        sd.snowflake(sd.get_point(self.x, self.y), self.length, color=sd.COLOR_WHITE)

    def can_fall(self):
        return self.y <= self.length


#
# flake = Snowflake()
# while True:
#     sd.start_drawing()
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if flake.can_fall():
#         break
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


def get_flakes(amount):
    new_flakes = []
    for _ in range(amount):
        new_flakes.append(Snowflake())
    return new_flakes


def get_fallen_flakes(flakes_list):
    count = 0
    for flake in flakes_list:
        if flake.can_fall():
            count += 1
    return count


def del_snowflakes(flakes):
    for flake in flakes:
        if flake.y < flake.length:
            flake.clear_previous_picture()
            flakes.remove(flake)


def add_more_flakes(number_of_flakes_to_add):
    flakes_to_add = []
    for number in range(number_of_flakes_to_add):
        flakes_to_add.append(Snowflake())
    return flakes_to_add


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(20)  # создать список снежинок

while True:
    sd.start_drawing()
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()  # подчитать сколько снежинок уже упало
    if get_fallen_flakes(flakes):
        flakes.extend(add_more_flakes(get_fallen_flakes(flakes)))
    del_snowflakes(flakes)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
