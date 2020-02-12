# -*- coding: utf-8 -*-

import simple_draw as sd


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


def draw_branches(start_point, angle, length):
    v1 = sd.get_vector(start_point, angle + 30, length, 3)
    v1.draw()
    v2 = sd.get_vector(start_point, angle - 30, length, 3)
    v2.draw()


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви


def draw_branches_2(start_point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point, angle + 30, length, 3)
    v1.draw()
    v2 = sd.get_vector(start_point, angle - 30, length, 3)
    v2.draw()
    draw_branches_2(v1.end_point, angle + 30, length * .75)
    draw_branches_2(v2.end_point, angle - 30, length * .75)


# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)


# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# I'll do it after finishing the first part of the task :)
# зачет!

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg


def draw_branches_3(start_point, angle, length):
    angle_shift = (30 * sd.random_number(-40, 40) / 100)
    length_shift = ((0.75 * sd.random_number(-20, 20)) / 100)
    if length < 5:
        return
    v1 = sd.get_vector(start_point, angle + 30, length, 3)
    v1.draw()
    v2 = sd.get_vector(start_point, angle - 30, length, 3)
    v2.draw()
    draw_branches_3(v1.end_point, angle + 30 + angle_shift, length * (.75 + - length_shift))
    draw_branches_3(v2.end_point, angle - 30 + angle_shift, length * (.75 + - length_shift))


draw_branches_3(sd.get_point(300, 30), angle=90, length=100)

# Пригодятся функции
# sd.random_number()

sd.pause()
