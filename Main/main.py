"""
Main loop

This is the main loop of the game
"""
import pygame as pg
import math
import track
import hitbox
import car
import checkpoints

# making the game window and loading images
pg.init()
clock = pg.time.Clock()
height = 720
width = 1280
h_half = height / 2
w_half = width / 2
win = pg.display.set_mode((width, height))
pg.display.set_caption("Car AI")


# draw window and other classes method
def window():
    # win.fill((0, 0, 0))
    cp.draw(win)
    t_out.draw(win)
    t_in.draw(win)
    h.draw(win, c.angle, c.position[0], c.position[1])
    c.draw(win)
    pg.display.flip()


# booleans to check if car is driving forward or backwards to fix steering
forward = True
backwards = False


# making objects
t_out = track.Track(((100, 392),
(100, 249),
(150, 171),
(237, 111),
(404, 95),
(594, 89),
(745, 95),
(793, 121),
(828, 178),
(833, 228),
(799, 286),
(740, 334),
(730, 365),
(812, 381),
(940, 385),
(1086, 397),
(1143, 441),
(1174, 502),
(1175, 574),
(1123, 643),
(1043, 669),
(845, 681),
(320, 675),
(199, 643),
(133, 571)))
t_in = track.Track(((236, 376),
                    (247, 260),
                    (289, 222),
                    (625, 205),
                    (681, 218),
                    (681, 229),
                    (636, 266),
                    (596, 341),
                    (596, 438),
                    (645, 473),
                    (726, 488),
                    (955, 501),
                    (980, 507),
                    (1005, 522),
                    (1008, 530),
                    (996, 550),
                    (786, 565),
                    (313, 548),
                    (267, 502)))
cp = checkpoints.Checkpoints() # values needed
h = hitbox.Hitbox()
c = car.Car()

done = False
# main game loop
while not done:
    # set clock speed of game
    clock.tick(60)

    # car_crash = pg.sprite.spritecollide(c, group, True, pg.sprite.collide_mask)

    car_crash = pg.sprite.collide_mask(c, t_out) or pg.sprite.collide_mask(c, t_in)

    if car_crash:
        print('collide')
        car_crash = False
        c.__init__()
    #
    # to check if game window has been closed
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    # check for input
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        c.speed -= c.acceleration
        forward = True
        backwards = False
    if keys[pg.K_DOWN]:
        c.speed += c.deceleration
        forward = False
        backwards = True
    # car can only turn if the car is moving
    if keys[pg.K_RIGHT] and abs(c.speed) > 0.1 and forward:
        c.angle -= c.turn_speed
    if keys[pg.K_LEFT] and abs(c.speed) > 0.1 and forward:
        c.angle += c.turn_speed
    if keys[pg.K_RIGHT] and abs(c.speed) > 0.1 and backwards:
        c.angle += c.turn_speed
    if keys[pg.K_LEFT] and abs(c.speed) > 0.1 and backwards:
        c.angle -= c.turn_speed
    #  handbrake for car
    if keys[pg.K_SPACE]:
        if c.speed < 0:
            c.speed += 0.3
        if c.speed > 0:
            c.speed -= 0.3

    # simulate momentum
    if not done:
        if c.speed < 0:
            c.speed += 0.08
        if c.speed > 0:
            c.speed -= 0.08

    # setting speed to 0 if the car's absolute speed value is under 0.1 to be able to fully stop car
    if abs(c.speed) < 0.1:
        c.speed = 0

    # to check if car reached maximum speed
    if c.speed > c.max_forward_speed:
        c.speed = c.max_forward_speed
    if c.speed < c.max_reverse_speed:
        c.speed = c.max_reverse_speed

    # works out rotation of car
    x, y = c.position
    rad = c.angle * math.pi / 180
    x += c.speed * math.sin(rad)
    y += c.speed * math.cos(rad)
    c.position = (x, y)

    window()

pg.quit()
