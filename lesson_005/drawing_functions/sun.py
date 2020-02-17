import simple_draw as sd

angle = 30


def draw_sun(x, y, length):
    global angle
    radius = length // 2
    sd.start_drawing()
    sd.vector(sd.get_point(x, y), angle=angle, length=length, color=sd.background_color, width=3)
    angle += 30
    sd.vector(sd.get_point(x, y), angle=angle, length=length, color=(255, 255, 0), width=3)
    sd.vector(sd.get_point(x, y), angle=angle + 30, length=length, color=(255, 255, 0), width=3)
    sd.vector(sd.get_point(x, y), angle=angle + 60, length=length, color=(255, 255, 0), width=3)
    sd.finish_drawing()
    sd.circle(sd.get_point(x, y), radius=radius, width=0)
    sd.sleep(0.01)


if __name__ == '__main__':
    draw_sun(150, 150, 150)
    sd.pause()
