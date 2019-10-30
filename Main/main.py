import pygame as pg
import math
import track
import hitbox
import car

pg.init()
background = pg.image.load("track.png")
image = pg.image.load("car.png")
clock = pg.time.Clock()
height = 720
width = 1280
h_half = height / 2
w_half = width / 2
win = pg.display.set_mode((width, height))
pg.display.set_caption("")


def window():
    win.blit(background, (0, 0))
    # h.draw(win, s.position[0], s.position[1])
    c.draw(win, image)
    h.draw(win, c.angle, c.position[0], c.position[1])
    pg.display.update()


forward = True
backwards = False
k_up = k_down = k_left = k_right = 0

t = track.Track()
h = hitbox.Hitbox()
c = car.Car()
done = False
while not done:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    keys = pg.key.get_pressed()

    if keys[pg.K_UP]:
        c.speed -= c.acceleration
        forward = True
        backwards = False
    if keys[pg.K_DOWN]:
        c.speed += c.deceleration
        forward = False
        backwards = True
    if keys[pg.K_RIGHT] and abs(c.speed) > 0.1 and forward:
        c.angle -= c.turn_speed
    if keys[pg.K_LEFT] and abs(c.speed) > 0.1 and forward:
        c.angle += c.turn_speed
    if keys[pg.K_RIGHT] and abs(c.speed) > 0.1 and backwards:
        c.angle += c.turn_speed
    if keys[pg.K_LEFT] and abs(c.speed) > 0.1 and backwards:
        c.angle -= c.turn_speed
    if keys[pg.K_SPACE]:
        if c.speed < 0:
            c.speed += 0.3
        if c.speed > 0:
            c.speed -= 0.3

    if not done:
        if c.speed < 0:
            c.speed += 0.08
        if c.speed > 0:
            c.speed -= 0.08

    if abs(c.speed) < 0.1:
        c.speed = 0

    if c.speed > c.max_forward_speed:
        c.speed = c.max_forward_speed
    if c.speed < c.max_reverse_speed:
        c.speed = c.max_reverse_speed

    x, y = c.position
    rad = c.angle * math.pi / 180
    x += c.speed * math.sin(rad)
    y += c.speed * math.cos(rad)
    c.position = (x, y)

    window()

pg.quit()
