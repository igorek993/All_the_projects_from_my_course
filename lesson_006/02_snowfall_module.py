# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка TODO I cant understand why I should create
#   todo 'список номеров снежинок' then show them on the screen and then delete them all from the same list???
# todo I can't also understand the point of making a list of escaped snowflakes and showing it in the console :)
# todo To make a long story short, I do not quite understand the last steps as they do not make sense to me....
# todo Would you be able to explain to me what I have to do a bit more clear? thank you!
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
# while True:
#  нарисовать_снежинки_цветом(color=sd.background_color)
#  сдвинуть_снежинки()
#  нарисовать_снежинки_цветом(color)
#  если есть номера_достигших_низа_экрана() то
#       удалить_снежинки(номера)
#       создать_снежинки(count)


from lesson_006.snowfall import create_snowflakes, draw_colored_snowflakes, move_snowflakes, \
    draw_background_snowflakes, escaped_snowflakes

create_snowflakes(20)
while True:
    draw_background_snowflakes()
    move_snowflakes()
    draw_colored_snowflakes(sd.COLOR_YELLOW)
    escaped_snowflakes()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
