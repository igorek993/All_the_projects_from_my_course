import simple_draw as sd


def draw_smile(point_x, point_y, color):
    x = point_x
    y = point_y
    color = color
    point = sd.get_point(x, y)
    sd.circle(center_position=point, color=color, width=8, radius=70)

    x_1 = x - 25
    y_1 = y + 20
    point_1 = sd.get_point(x_1, y_1)
    sd.circle(center_position=point_1, radius=8, width=0, color=color)

    x_2 = x + 25
    y_2 = y + 20
    point_2 = sd.get_point(x_2, y_2)
    sd.circle(center_position=point_2, radius=8, width=0, color=color)

    x_3 = x - 35
    y_3 = y - 20
    point_3 = sd.get_point(x_3, y_3)

    x_4 = x - 15
    y_4 = y - 30
    point_4 = sd.get_point(x_4, y_4)

    x_5 = x + 15
    y_5 = y - 30
    point_5 = sd.get_point(x_5, y_5)

    x_6 = x + 25
    y_6 = y - 20
    point_6 = sd.get_point(x_6, y_6)

    point_list = [point_3, point_4, point_5, point_6]
    sd.lines(point_list=point_list, color=color, width=4)
