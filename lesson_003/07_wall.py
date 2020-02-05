# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.set_screen_size(600, 675)
square_point = sd.get_point(0,0)
sd.square(square_point, side=1000, color=(127, 63, 0))
left_x =0
left_y = -52
right_x= 100
right_y= -2
for _ in range (15):
    right_x = 100
    left_x = 0
    left_y +=104
    right_y+=104
    for _ in range(10):
        left_bottom_point = sd.get_point(left_x,left_y)
        right_top_point = sd.get_point(right_x,right_y)
        sd.rectangle(left_bottom_point, right_top_point, color=(0, 0, 255))
        left_x+=102
        right_x +=102

left_x =0
left_y = -105
right_x= 100
right_y= -53
for _ in range (15):
    right_x = 50
    left_x = -50
    left_y +=104
    right_y+=104
    for _ in range(10):
        left_bottom_point = sd.get_point(left_x,left_y)
        right_top_point = sd.get_point(right_x,right_y)
        sd.rectangle(left_bottom_point, right_top_point, color=(0, 0, 255))
        left_x+=102
        right_x +=102


sd.pause()
