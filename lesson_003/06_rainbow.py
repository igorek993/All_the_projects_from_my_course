# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# TODO Выполнненые тудушки надо убирать
x=50
y=50
z=350
j=450
for colour in rainbow_colors:
    point_1 = sd.get_point(x, y)
    point_2 = sd.get_point(z, j)
    sd.line(point_1, point_2, color=colour, width=4)
    x+=5
    y+=5
    z+=5
    j+=5
 # TODO РЕР8!

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.get_point(0,0)  # TODO РЕР8!
radius = 400
for colour in rainbow_colors:
    radius+=20
    # TODO РЕР8!
    sd.circle(center_position=point,radius=radius,color=colour, width=20)

sd.pause()
