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
    while True:
        x = []
        for _ in range(20):
            x.append(sd.random_number(0, sd.resolution[0]))
        y = []
        for _ in range(20):
            y.append(sd.random_number(sd.resolution[1] - (sd.resolution[1] / 2), sd.resolution[1]))
        flake_length = []
        for _ in range(20):
            flake_length.append(sd.random_number(20, 100))
        x_1 = []
        y_2 = []
        for point_1, point_2, length in zip(x, y, flake_length):
            sd.snowflake(sd.get_point(point_1, point_2), length)
            x_1.append(point_1 + sd.random_number(1, 15))
            y_2.append(point_2 - sd.random_number(1, 30))
        sd.sleep(0.1)
        sd.clear_screen()
        while True:
            sd.clear_screen()
            for point_1, point_2, length in zip(x_1, y_2, flake_length):
                sd.snowflake(sd.get_point(point_1, point_2), length)
            sd.sleep(0.1)
            for a, b in enumerate(x_1):
                x_1[a] += sd.random_number(-30, 30)
            for a, b in enumerate(y_2):
                y_2[a] -= sd.random_number(10, 30)
            sd.sleep(0.1)
            for a, b in enumerate(y_2):
                if y_2[a] < -80:
                    y_2[a] = (sd.random_number(sd.resolution[1] - (sd.resolution[1] / 2), sd.resolution[1]))
            else:
                continue
            if sd.user_want_exit():
                break
# TODO Очень всё избыточно и запутано. Надо проще.
#  1) До основного цикла заполняем данные о снежинках: координаты и размеры. Так как эти списки имеют один размер (по
#  числу снежинок), то заполнять все три списка можно в одном цикле. Названия переменных должны говорить о том что там
#  находится (просто "икс" говорит о том, что там одна координата, а не список).
#  2) Далее, основной цикл while True:, всё верно, а внутри него находятся:
#        а) очистка экрана
#        б) ОДИН for итерирующий по снежинкам. Этот for отрисовывает один кадр "мультфильма" Снегопад.
#        в) sd.sleep(0.1)
#        г) и проверка "не желает ли пользователь выйти"
# 3) Внутри цикла for перебираем по очереди снежинки, и проверяем, а не лежит ли снежинка на земле? если нет, то
# сдвигаем её (уменьшаем ей игрек)
# Далее - отрисовываем текущую снежинку.
# Всё просто и логично :)

# I haven't finished yet, just wanted you to take a look at it first to optimize the code a little bit
# so I can start thinking on the second part. Thank you!

snow()

sd.pause(x, y)

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
