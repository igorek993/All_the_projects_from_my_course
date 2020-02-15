# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.


import simple_draw as sd
from lesson_005.drawing_functions.wall_with_a_window import draw_wall_with_a_window
from lesson_005.drawing_functions.triangle import triangle_2


def draw_house_with_a_roof(house_width_range, house_height_range):
    draw_wall_with_a_window(house_width_range, house_height_range)
    triangle_2(sd.get_point((house_width_range[0] - 50), (house_height_range[-1])), 0,
               length=((house_width_range[-1] + 50) - house_width_range[0]), color=(255, 255, 102))


if __name__ == '__main__':
    sd.set_screen_size(1600, 1000)
    house_width_range = range(400, 900)
    house_height_range = range(100, 500)
    draw_house_with_a_roof(house_width_range, house_height_range)

    sd.pause()
