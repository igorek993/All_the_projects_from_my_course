import simple_draw as sd


def draw_rainbow(point, radius):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    for colour in rainbow_colors:
        radius += 20
        sd.circle(center_position=point, radius=radius, color=colour, width=20)


if __name__ == '__main__':
    point = sd.get_point(0, 0)
    radius = 400
    draw_rainbow(point, radius)
    sd.pause()
