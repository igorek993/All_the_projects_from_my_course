# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)


# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

import simple_draw as sd
from lesson_005.drawing_functions.brick_house import draw_house_with_a_roof
from lesson_005.drawing_functions.smile import draw_smile
from lesson_005.drawing_functions.snowflakes import draw_snow
from lesson_005.drawing_functions.tree import draw_tree
from lesson_005.drawing_functions.rainbow import draw_rainbow
from lesson_005.drawing_functions.sun import draw_sun

sd.set_screen_size(1600, 1000)

house_width_range = range(400, 900)
house_height_range = range(100, 500)

draw_house_with_a_roof(house_width_range, house_height_range)
draw_smile(700, 300, color=(255, 255, 0))
sd.rectangle((sd.get_point(350, 0)), (sd.get_point(1600, 100)), width=0, color=(0, 255, 0))
# TODO Try to use the sd.start/finish_drawing() functions for the fractal tree
draw_tree(sd.get_point(1300, 100), angle=90, length=100)
draw_rainbow(sd.get_point(420, 100), 1200)
while True:
    draw_sun(150, 800, 150)
    # draw_snow()
    if sd.user_want_exit():
        break

#  So I got stuck here because I cant understand how I should change the animated functions so they only reproduce
#  one loop and then start over and over again? If you take a look at my code now, the snow will never start falling
#  down because there is a while True loop in the previous function, but if I get rid of it, the sun won't be
#  animated... so the question is: how to make two animations work at the same time? I do not understand the way
#  I should edit the code inside the actual function e.g. 'draw_sun' or 'draw_snow' Thank you!
# TODO First of all you should make sun animation in the right way. See my comments at the sun.py module.
sd.pause()
