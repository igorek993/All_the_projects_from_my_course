import simple_draw as sd


def draw_tree(start_point, angle, length):
    color = (0, 153, 0)
    angle_shift = (30 * sd.random_number(-40, 40) / 100)
    length_shift = ((0.75 * sd.random_number(-20, 20)) / 100)
    if length < 8:
        return
    v1 = sd.get_vector(start_point, angle + 30, length, 3)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point, angle - 30, length, 3)
    v2.draw(color=color)
    draw_tree(v1.end_point, angle + 30 + angle_shift, length * (.75 + - length_shift))
    draw_tree(v2.end_point, angle - 30 + angle_shift, length * (.75 + - length_shift))
