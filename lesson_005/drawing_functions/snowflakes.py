import simple_draw as sd


def draw_snow(x_list, y_list, flake_length_list, number_of_snowflakes):
    for _ in range(number_of_snowflakes):  # TODO Чуть не зачёл, но увидев это! :) Интересно, что вы осознаёте что этот
        # цикл не нужен (раз после первой же итерации делаете break), но почему-то его оставили....
        x_list.append(sd.random_number(0, 310))
        y_list.append(sd.random_number(200, 500))
        flake_length_list.append(sd.random_number(20, 50))
        sd.start_drawing()
        for x, y, length, i in zip(x_list, y_list, flake_length_list, range(number_of_snowflakes)):
            if y_list[i] > 65:
                sd.snowflake(sd.get_point(x, y), length, color=sd.background_color)
            x_list[i] += sd.random_number(-15, 15)
            y_list[i] -= sd.random_number(4, 30)
            if y_list[i] < 50:
                y_list[i] = sd.random_number(300, 600)
            if x_list[i] > 310:
                x_list[i] = x_list[i] - 20
            sd.snowflake(sd.get_point(x_list[i], y_list[i]), length)
        sd.finish_drawing()
        sd.sleep(0.1)
        break
