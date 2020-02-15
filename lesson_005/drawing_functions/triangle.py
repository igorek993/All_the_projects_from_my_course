import simple_draw as sd


def draw_a_shape(start_point, angle, length, number_of_sides, color):
    current_point = start_point
    max_angle = 360 + angle
    angle_step = 360 // number_of_sides
    for angle in range(angle, max_angle, angle_step):
        current_vector = sd.get_vector(current_point, angle, length, 3)
        sd.vector(current_point, angle, length, color=color, width=5)
        current_point = current_vector.end_point


def triangle_2(start_point, angle, length, color):
    draw_a_shape(start_point, angle, length, 3, color=color)


def draw_triangle(point1, point2, point3):
    vector1 = pointpa2 - point1


if __name__ == '__main__':
    triangle_2(sd.get_point(100, 100), 0, 100, color=(255, 255, 0))
    sd.pause()
