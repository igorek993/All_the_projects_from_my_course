import simple_draw as sd


def draw_rainbow(point, radius_shift):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    colour = rainbow_colors[sd.random_number(0, 6)]
    sd.circle(center_position=point, radius=radius_shift, color=colour, width=20)


if __name__ == '__main__':
    point = sd.get_point(0, 0)
    radius = 400
    draw_rainbow(point, radius)
    sd.pause()
