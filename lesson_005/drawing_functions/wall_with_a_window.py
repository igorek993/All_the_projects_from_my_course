import simple_draw as sd


def draw_wall_with_a_window(house_width_range, house_height_range):
    brick_width = 100
    brick_height = 50
    row = 0
    color = (255, 51, 51)
    for y in house_height_range[::brick_height]:
        row += 1
        shift_x = 0 if row % 2 else brick_width // 2
        for x in house_width_range[::brick_width]:
            x -= shift_x
            sd.rectangle(sd.get_point(x, y), sd.get_point(x + brick_width, y + brick_height), color=color,
                         width=3)
    sd.rectangle((sd.get_point(house_width_range[0] - 50, house_height_range[0])),
                 (sd.get_point(house_width_range[-1], house_height_range[-1])), color=color, width=3)
    sd.rectangle((sd.get_point(house_width_range[0] + 100, house_height_range[0] + 100)),
                 (sd.get_point(house_width_range[-1] - 100, house_height_range[-1] - 100)), color=(204, 255, 255),
                 width=0)


if __name__ == "__main__":
    print("I am not being imported")
    sd.set_screen_size(1600, 900)
    house_width_range = range(300, 900)
    house_height_range = range(100, 600)
    draw_wall_with_a_window(house_width_range, house_height_range)

    sd.pause()
