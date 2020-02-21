import simple_draw as sd

x_list = []
y_list = []
flake_length_list = []
sd.resolution = (1200, 900)
number_escaped_snowflakes = []


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
    global number_escaped_snowflakes
    number_escaped_snowflakes = []
    for _ in range(number):
        if y_list[_] <= 0:
            number_escaped_snowflakes.append(_)
            print(number_escaped_snowflakes)


def delete_from_list(*args):
    global number_escaped_snowflakes
    args = list(args)
    for i in args:
        number_escaped_snowflakes.remove(i)
    print(number_escaped_snowflakes)
