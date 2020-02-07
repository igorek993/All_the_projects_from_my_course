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
row = 0
for y in range(0, sd.resolution[1], brick_height):
    sd.rectangle(left_bottom_point, right_top_point, color=(255, 127, 0), width=3)
    row += 1
    if row % 2:
        shift_x = 0
    else:
        shift_x = brick_width // 2
    for x in range(0, sd.resolution[0], brick_width):
        x = x - shift_x
        left_bottom_point = sd.get_point(x, y)
        right_top_point = sd.get_point(x + brick_width, y + brick_height)
        sd.rectangle(left_bottom_point, right_top_point, color=(255, 127, 0), width=3)

sd.pause()
