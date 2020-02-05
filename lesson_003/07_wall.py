# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# TODO Во всём файле поправьте стиль кода (см. РЕР8). Можно воспользоваться меню Пайчарма - Code/Reformat Code

# TODO Введите константы с размерами кирпича. В коде кругом, где можно нужно использовать переменные, константы или
#  данные полученные программно - так делается гибкий код. При изменении любого параметра будет достаточно это сделать
#  в одном месте - вверху модуля (файла с кодом), где находятся константы, а не выискивать число по всему коду.

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
# TODO Код

#  ПОДСКАЗКА
#  Как работал бы человек если ему надо заложить
#  окно кирпичами? Он начал бы из нижего левого угла (координаты х = 0, у = 0) и по пордяку
#  клал бы ряд (наращивая только "х = х + brick_width) до правой границы окна
#  ("у = 0" сохраняется). Потом, перешёл бы ко второму ряду (т.е.  у = у + brick_height, x = 0)
#  и процесс повторяется. Тут явно видны два вложенных цикла for, "верхний" по координате "у",
#  а вложенный по коордитане "x". Для цикла for по "у" итерируем по range(0, sd.resolution[1], brick_height,
#  а для "х" сами допишите, пожалуйста. Чётные ряды нужно сдвигать на полкирпича.


sd.pause()
