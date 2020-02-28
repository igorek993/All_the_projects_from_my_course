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

def get_flakes(count):
    flakes = []
    for number in range(count):
        flakes.append(Snowflake())
    return flakes


def get_fallen_flakes():
    global flakes
    # TODO Чтобы не использовать переменные из внешней области видимости - передавайте список снежинок через аргумент
    #  функции
    count = 0
    for flake in flakes:
        if flake.can_fall():
            count += 1
    return count


def append_flakes(count):
    global flakes
    for number in range(count):
        flakes.append(Snowflake())
    # TODO Это не замечание, это к размышлению: сравните эту функцию и get_flakes, в чём разница? Первая не испльзует
    #  ничего из глобальной области видимости и поэтому она может считаться чистой функцией. Попытайтесь использовать
    #  именно её в главном цикле основного кода для добавления новых снежинок.

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=3)  # создать список снежинок

while True:
    sd.start_drawing()
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
        # TODO Заметили как лавинообразно нарастает кол-во новых снежинок? Чтобы этого не было, надо удалять из списка
        #  упавшие снежинки - создайте такую функцию
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
