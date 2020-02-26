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
        if y_list[index] <= -flake_length_list[index]:
            number_escaped_snowflakes.append(index)
    return number_escaped_snowflakes


def delete_snowflakes(number_escaped_snowflakes):
    global x_list
    global y_list
    global flake_length_list
    for index in number_escaped_snowflakes:
        x_list.insert(index, 0)
        y_list.insert(index, 0)
        # TODO Нет. Представьте что у вас две снежинки упали: № 2 и № 5. Если удалить 2ю, а потом 5ю, то удалится 6я,
        #  так? А если поменять подход и 5ю удалить первой, а 2ю после, будет ошибка в индексе?
        # I do not think it is going to affect any other flake as far as I can see it... because it crates a new
        # variable prior to deleting each flake that does not allow it to change its index. I am not really
        # sure what is the other way of doing this. I think I might need a tip in this case:)
        # TODO Видимо слишком кратко пояснил. Хотел сказать, что ваш вариант конечно рабочий, но не очень удачный.
        #  Вы ставляете "пустышку", потом удаляете с учётом сдвига. Функция удаления не должна ничего всталять: "одна
        #  функция, одно дело за которое она отвечает", "называние должно чётко отражать то что делает функция".
        #  Выше предложил подумать как можно удалять не влияя на ещё не удалённые элементы, кажется вы не прокрутили в
        #  голове описанное выше "упражнение" со снежинкой № 2 и № 5. Немного переформулировал предыдущую тудушку.
        flake_length_list.insert(index, 0)
        del x_list[index + 1]
        del y_list[index + 1]
        del flake_length_list[index + 1]


def add_snowflakes(number_escaped_snowflakes):
    global x_list
    global y_list
    global flake_length_list
    for index in number_escaped_snowflakes:
        x_list[index] = (sd.random_number(0, sd.resolution[0]))
        y_list[index] = (sd.random_number(sd.resolution[1], sd.resolution[1] * 2))
        flake_length_list[index] = (sd.random_number(20, 50))
