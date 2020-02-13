# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 900)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


def snow():
    x_list = []
    y_list = []
    flake_length_list = []
    number_of_snowflakes = 20
    for _ in range(number_of_snowflakes):
        x_list.append(sd.random_number(0, sd.resolution[0]))
        y_list.append(sd.random_number(sd.resolution[1] * 0.5, sd.resolution[1]))
        flake_length_list.append(sd.random_number(20, 50))
    while True:
        sd.start_drawing()
        for x, y, length, i in zip(x_list, y_list, flake_length_list, range(number_of_snowflakes)):
            if y_list[i] > 65:
                sd.snowflake(sd.get_point(x, y), length, color=sd.background_color)
            x_list[i] += sd.random_number(-15, 15)
            y_list[i] -= sd.random_number(4, 30)
            if y_list[i] < 50:
                y_list[i] = sd.random_number((sd.resolution[1] * 0.5), sd.resolution[1])
            sd.snowflake(sd.get_point(x_list[i], y_list[i]), length)
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break


snow()

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
