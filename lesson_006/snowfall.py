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


def delete_and_add_snowflakes(number_escaped_snowflakes):
    global x_list
    global y_list
    global flake_length_list
    for index in number_escaped_snowflakes:
        x_list.insert(index, (sd.random_number(0, sd.resolution[0])))
        y_list.insert(index, sd.random_number(sd.resolution[1], sd.resolution[1] * 2))
        flake_length_list.insert(index, sd.random_number(20, 50))
        del x_list[index + 1]
        del y_list[index + 1]
        del flake_length_list[index + 1]
