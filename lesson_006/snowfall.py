import simple_draw as sd

x_list = []
y_list = []
flake_length_list = []
sd.resolution = (1200, 900)


def create_snowflakes(n):
    global number
    number = n
    for _ in range(number):
        x_list.append(sd.random_number(0, sd.resolution[0]))
        y_list.append(sd.random_number(sd.resolution[1], sd.resolution[1] * 2))
        flake_length_list.append(sd.random_number(20, 50))


def draw_background_snowflakes():
    sd.start_drawing()
    for x, y, length in zip(x_list, y_list, flake_length_list):
        sd.snowflake(sd.get_point(x, y), length, color=sd.background_color)


def move_snowflakes():
    for i in range(number):
        x_list[i] += sd.random_number(-15, 15)
        y_list[i] -= sd.random_number(4, 30)


def draw_colored_snowflakes(color):
    for x, y, length in zip(x_list, y_list, flake_length_list):
        sd.snowflake(sd.get_point(x, y), length, color=color)
    sd.finish_drawing()


def escaped_snowflakes():
    number_escaped_snowflakes = []
    for index in range(number):
        if y_list[index] <= -50:  # TOdO  Вместо числа тут следует использовать размер снежинки
            number_escaped_snowflakes.append(index)
    return number_escaped_snowflakes


def delete_from_list(number_escaped_snowflakes):
    global x_list
    global y_list
    global flake_length_list
    count_to_add = 0
    for index in number_escaped_snowflakes:
        # TODO Замечаете что некоторые снежинки пропадают с экрана ещё не долетев но низа? Уберите стирание упавших в
        #  основном цикле снегопада (именно упавших) и заметите, что они замирают в середине экрана. Это происходит от
        #  того, что при удалении "снежинки" из середины списка, вся вторая половниа списка получает новые номера
        #  элементов, на единицу меньше, согласны? И после этого удаление из второй половины списка происходит не
        #  корректно. Поправить это можно слегка изменив порядок удаления. Догадайтесь сами как при удалении никогда не
        #  попадать во "вторую" половниу списка, а только в "первую".
        del x_list[index]
        del y_list[index]
        del flake_length_list[index]
        count_to_add = count_to_add + 1
    return count_to_add


def add_new_snowflakes(count_to_add):
    global x_list
    global y_list
    global flake_length_list
    for number in range(count_to_add):
        x_list.append(sd.random_number(0, sd.resolution[0]))
        y_list.append(sd.random_number(sd.resolution[1], sd.resolution[1] * 2))
        flake_length_list.append(sd.random_number(20, 50))
