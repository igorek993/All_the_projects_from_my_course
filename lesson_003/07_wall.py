# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

brick_width = 100
brick_height = 50
x = 0
y = 0
left_bottom_point = sd.get_point(x, y)
right_top_point = sd.get_point(x + brick_width, y + brick_height)
# TODO Эти четыре строки выше не нужны
row = 0
for y in range(0, sd.resolution[1], brick_height):
    sd.rectangle(left_bottom_point, right_top_point, color=(255, 127, 0), width=3)
    # TODO эта строка не нужна, она дублирует вывод последнего кирпича из предыдущего ряда

    row += 1
    # if row % 2:
    #     shift_x = 0
    # else:
    #     shift_x = brick_width // 2
    # А теперь смотрите как тоже самое делае тернарный оператор:
    shift_x = brick_width // 2 if row % 2 else 0
    for x in range(0, sd.resolution[0], brick_width):
        x -= shift_x
        left_bottom_point = sd.get_point(x, y)
        right_top_point = sd.get_point(x + brick_width, y + brick_height)
        sd.rectangle(left_bottom_point, right_top_point, color=(255, 127, 0), width=3)

sd.pause()

