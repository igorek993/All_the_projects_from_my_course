# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

square_point = sd.get_point(0, 0)
sd.square(square_point, side=1000, color=(127, 63, 0))
brick_width = 100
brick_height = 50
left_x = -100
left_y = -50
right_x = left_x + brick_width
right_y = left_y + brick_height
left_bottom_point = sd.get_point(left_x, left_y)
right_top_point = sd.get_point(right_x, right_y)
sd.rectangle(left_bottom_point, right_top_point, color=(0, 0, 0), width=3)

for _ in range(14):
    left_x = -100
    left_y = left_y + brick_height
    for _ in range(15):
        left_x = left_x + brick_width
        left_bottom_point = sd.get_point(left_x, left_y)
        sd.rectangle(left_bottom_point, right_top_point, color=(0, 0, 0), width=3)

# I am really sorry, but I genuinely can´t understand the way I should write this code properly. I can't get
# how I can use even and odd numbers because we have never done anything with them so far. The second thing I cant
# understand is why the first brick changes its colour if I use 0,0 coordinate, so I just made them negative. I can't
# even really phrase those question that I have cause they are all small and really detailed. I would highly appreciate if
# you could give me more hints on how to make this code work in a way it should. The last issue is my time zone
# (I live in Melbourne) which is so different to yours, I only have a bit of time every evening to ask questions in
# our telegram channel. Thank you!

#  ПОДСКАЗКА
#  Как работал бы человек если ему надо заложить
#  окно кирпичами? Он начал бы из нижего левого угла (координаты х = 0, у = 0) и по пордяку
#  клал бы ряд (наращивая только "х = х + brick_width) до правой границы окна
#  ("у = 0" сохраняется). Потом, перешёл бы ко второму ряду (т.е.  у = у + brick_height, x = 0)
#  и процесс повторяется. Тут явно видны два вложенных цикла for, "верхний" по координате "у",
#  а вложенный по коордитане "x". Для цикла for по "у" итерируем по range(0, sd.resolution[1], brick_height,
#  а для "х" сами допишите, пожалуйста. Чётные ряды нужно сдвигать на полкирпича.

# Another example of my code

for _ in range(14):
    left_x = -100
    left_y = left_y + brick_height
    for _ in range(10):
        a = 5
        a = a + 1
        if a % 2 == 1:
            left_x = left_x + brick_width
            left_bottom_point = sd.get_point(left_x, left_y)
            sd.rectangle(left_bottom_point, right_top_point, color=(0, 0, 0), width=3)
        elif a % 2 == 0:
            left_x = left_x + brick_width
            left_bottom_point = sd.get_point(left_x, left_y)
            sd.rectangle(left_bottom_point, right_top_point, color=(0, 0, 0), width=3)

sd.pause()
