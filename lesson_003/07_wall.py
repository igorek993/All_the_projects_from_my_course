# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

brick_width = 100
brick_height = 50
row = 0
for y in range(0, sd.resolution[1], brick_height):
    row += 1
    shift_x = 0 if row % 2 else brick_width // 2
    for x in range(0, sd.resolution[0], brick_width):
        x -= shift_x
        sd.rectangle(sd.get_point(x, y), sd.get_point(x + brick_width, y + brick_height), color=(255, 127, 0), width=3)

sd.pause()

# This code looks way better and easier than the one from my first attempt :D. Thank you for checking it!

# зачет!
