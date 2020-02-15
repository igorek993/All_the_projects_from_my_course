import simple_draw as sd

angle = 30


def draw_sun(x, y, length):
    angle = 30
    radius = length // 2
    while True:  # TODO What do you think, when this cycle will be finished? You should remove it, this function draws
        # only one-step picture (кадр движения), not an endless motion!! One new step!
        sd.start_drawing()
        for _ in range(1):
            sd.vector(sd.get_point(x, y), angle=angle, length=length, color=sd.background_color, width=3)
            angle += 30
            sd.vector(sd.get_point(x, y), angle=angle, length=length, color=(255, 255, 0), width=3)
            sd.vector(sd.get_point(x, y), angle=angle + 30, length=length, color=(255, 255, 0), width=3)
            sd.vector(sd.get_point(x, y), angle=angle + 60, length=length, color=(255, 255, 0), width=3)

            sd.finish_drawing()   # TODO These three lines should be on the same level as the sd.start_drawing()
            sd.circle(sd.get_point(x, y), radius=radius, width=0)
            sd.sleep(0.1)

        if sd.user_want_exit():  # todo  kill this, you already have it in the main cycle
            break


if __name__ == '__main__':
    draw_sun(150, 150, 150)
    sd.pause()
