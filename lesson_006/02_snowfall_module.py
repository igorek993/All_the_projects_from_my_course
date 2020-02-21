# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
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
    draw_background_snowflakes, escaped_snowflakes, delete_from_list

create_snowflakes(20)
while True:
    draw_background_snowflakes()
    move_snowflakes()
    draw_colored_snowflakes(sd.COLOR_YELLOW)
    escaped_snowflakes()
    sd.sleep(0.1)
    if sd.user_want_exit():
        delete_from_list(0, 5, 7, 2, 6)
        break
sd.pause()