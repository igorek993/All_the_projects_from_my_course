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

def get_flakes(first_amount, amount_to_add):
    global flakes
    if not flakes:
        for number in range(first_amount):
            flakes.append(Snowflake())
        return flakes
    elif amount_to_add > 0:
        for number in range(amount_to_add):
            flakes.append(Snowflake())


def get_fallen_flakes(flakes_list):
    flakes = flakes_list
    count = 0
    for flake in flakes:
        if flake.can_fall():
            count += 1
    return count


def del_snowflakes():
    global flakes
    for flake in flakes:
        if flake.y < flake.length:
            flake.clear_previous_picture()
            flakes.remove(flake)


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = []  # создать список снежинок

while True:
    sd.start_drawing()
    get_flakes(20, 0)
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes(flakes)  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        get_flakes(1, amount_to_add=fallen_flakes)  # добавить еще сверху#
        del_snowflakes()
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
