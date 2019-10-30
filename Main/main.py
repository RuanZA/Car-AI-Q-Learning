import pygame as pg
import math

pg.init()
image = pg.image.load("car.png")
clock = pg.time.Clock()
height = 720
width = 1280
h_half = height / 2
w_half = width / 2
win = pg.display.set_mode((width, height))
pg.display.set_caption("")


class Track(object):
    def __init__(self):
        pass

    def draw(self):
        pass


class Car(object):
    def __init__(self, x=250, y=250, angle=0.0, speed=0, deceleration=1, acceleration=1):
        self.position = (x, y)
        self.angle = angle
        self.speed = speed
        self.deceleration = deceleration
        self.acceleration = acceleration
        self.turn_speed = 5
        self.max_forward_speed = 5
        self.max_reverse_speed = -10
        self.throtle = False

    def draw(self, w, i):
        rotated = pg.transform.rotate(i, s.angle)
        rect = rotated.get_rect()
        rect.center = s.position
        print(s.angle)
        print(s.position)
        print(s.speed)
        w.blit(rotated, rect)
        pg.display.flip()


class Hitbox(object):
    def __init__(self, x=250, y=250):
        self.x = x
        self.y = y

    def draw(self, w):
        pg.draw.polygon(w, (255, 0, 0), s.position, 1)


def window():
    win.fill((0, 0, 0))
    s.draw(win, image)
    h.draw(win)
    pg.display.update()


k_up = k_down = k_left = k_right = 0
h = Hitbox()
s = Car()
done = False
while not done:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    keys = pg.key.get_pressed()

    if keys[pg.K_UP]:
        s.speed -= s.acceleration
    if keys[pg.K_DOWN]:
        s.speed += s.deceleration
    if keys[pg.K_RIGHT] and abs(s.speed) > 0.1:
        s.angle -= s.turn_speed
    if keys[pg.K_LEFT] and abs(s.speed) > 0.1:
        s.angle += s.turn_speed

    if not done:
        if s.speed < 0:
            s.speed += 0.08
        if s.speed > 0:
            s.speed -= 0.08

    if abs(s.speed) < 0.1:
        s.speed = 0

    if s.speed > s.max_forward_speed:
        s.speed = s.max_forward_speed
    if s.speed < s.max_reverse_speed:
        s.speed = s.max_reverse_speed

    x, y = s.position
    rad = s.angle * math.pi / 180
    x += s.speed * math.sin(rad)
    y += s.speed * math.cos(rad)

    s.position = (x, y)

    window()

pg.quit()
