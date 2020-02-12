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
    for _ in range(20):
        x_list.append(sd.random_number(0, sd.resolution[0]))
        y_list.append(sd.random_number(sd.resolution[1] - (sd.resolution[1] / 2), sd.resolution[1]))
        # TODO Просто возьмите половину числа, зачем же из целого вычитать половину? Кстати целочисленное деление это //
        #  Про это речь: sd.resolution[1] - (sd.resolution[1] / 2)
        flake_length_list.append(sd.random_number(20, 100))
    while True:
        sd.clear_screen()
        for point_1, point_2, length in zip(x_list, y_list, flake_length_list):  # Отлично, распаковка это удобно!
            # TODO point_1 это не точка, это координата икс текущей снежинки, вот тут очень удобно взять переменную "х"
            #  (и с игреком аналогично)
            sd.snowflake(sd.get_point(point_1, point_2), length)
            for a, b in enumerate(x_list):  # TODO Этот и ещё два, что ниже, циклы не нужны. Предыдущий for уже
                # "работает" с текущей снежинкой, вот её и обрабатывайте. А так выходит вы N*N раз делаете одно и тоже.
                # Ещё раз - сами циклы не нужны, а то что в их "телах" оставьте
                x_list[a] += sd.random_number(-15, 15)
            for a, b in enumerate(y_list):
                y_list[a] -= sd.random_number(0, 2)
            for a, b in enumerate(y_list):
                if y_list[a] < -40:
                    y_list[a] = (sd.random_number(sd.resolution[1] - (sd.resolution[1] / 2), sd.resolution[1]))
        sd.sleep(0.1)
        if sd.user_want_exit():
            break


#  Question. I think I followed your instructions and the code looks better now. What do you think? I am a
#  bit confused with the animation that became a lot faster even though I did not change the Y parameter at all, but I
#  still had to put it down to (0-2) in (((y_list[a] -= sd.random_number(0, 2)))).
# TODO да, уже много лучше. Только вот с вложенными в for дополнительными for перебор!

#  question 2. I tried to apply this advise (для ускорения отрисовки можно) and I cant figure out where I have to
#  place this bit (на старом месте снежинки отрисовать её же, но цветом sd.background_color) inside my code.
#  If you could help me with that, it would be wonderful. Thank you!
# TODO Там где сейчас стирание экрана, там вызывать sd.start_drawing (то есть до for), а после for - sd.finish...
#  Внутри for нужно теперь стирать снежинки с прерыдущего кадра цветом фона, потом сдивигать, и после этого уже рисовать
#  белым цветом. Вот и вся хитрость

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
