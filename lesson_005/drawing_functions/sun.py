import simple_draw as sd


def draw_sun(x, y, length):
    angle = 30
    radius = length // 2
    while True:
        sd.start_drawing()
        for _ in range(1):
            sd.vector(sd.get_point(x, y), angle=angle, length=length, color=sd.background_color, width=3)
            angle += 30
            sd.vector(sd.get_point(x, y), angle=angle, length=length, color=(255, 255, 0), width=3)
            sd.vector(sd.get_point(x, y), angle=angle + 30, length=length, color=(255, 255, 0), width=3)
            sd.vector(sd.get_point(x, y), angle=angle + 60, length=length, color=(255, 255, 0), width=3)
            sd.finish_drawing()
            sd.circle(sd.get_point(x, y), radius=radius, width=0)
            sd.sleep(0.1)
        if sd.user_want_exit():
            break


if __name__ == '__main__':
    draw_sun(150, 150, 150)
    sd.pause()
