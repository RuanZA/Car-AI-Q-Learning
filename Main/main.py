"""
Main loop

This is the main loop of the game
"""

import pygame as pg
import math
import track
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


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       div += 1

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    x = min(x, width)
    x = max(x, -width)

    y = min(y, width)
    y = max(y, -width)

    return x, y


def distance(point_a, point_b):
    # print(math.sqrt(math.pow((point_a[0] - point_b[0]), 2) + math.pow((point_a[1] - point_b[1]), 2)))
    return math.sqrt(math.pow((point_a[0] - point_b[0]), 2) + math.pow(point_a[1] - point_b[1], 2))


# draw window and other classes method
def window():
    win.fill((0, 0, 0))
    a = 0
    out_points = []
    for h in range(8):
        p1 = car.position[0] + math.cos(math.radians(-car.angle + a)) * 150
        p2 = car.position[1] + math.sin(math.radians(-car.angle + a)) * 150
        a += 45
        # out_points.append((car.position[0], car.position[1], p1, p2))
        out_points.append((p1, p2))
        # out_points.append((p1, p2))
    # for f in out_points:
    #     print(f)
    collider_point = []
    for tp in out_points:
        for tout in range(len(track_out) - 1):
            collider_point.append(line_intersection((car.position, tp), (track_out[tout], track_out[tout + 1])))
        for tin in range(len(track_in) - 1):
            collider_point.append(line_intersection((car.position, tp), (track_in[tin], track_in[tin + 1])))

    for p in collider_point:

        tempPoint = (p[0] - car.position[0], p[1] - car.position[1])
        if math.sqrt(tempPoint[0] * tempPoint[0] + tempPoint[1] * tempPoint[1]) > 150:
            continue
        # # pg.draw.circle(win, (255, 0, 0), (math.floor(p[0]), math.floor(p[1])), 3, 3)
        for tout in range(len(track_out) - 1):
            if distance(track_out[tout], p) + distance(track_out[tout + 1], p) == distance(track_out[tout], track_out[tout + 1]):
                pg.draw.circle(win, (255, 0, 0), (int(p[0]), int(p[1])), 3, 3)
                break
        for tin in range(len(track_in) - 1):
            if distance(track_in[tin], p) + distance(track_in[tin + 1], p) == distance(track_in[tin], track_in[tin + 1]):
                pg.draw.circle(win, (255, 0, 0), (int(p[0]), int(p[1])), 3, 3)
                break

    for d in out_points:
        pg.draw.line(win, (255, 0, 0), car.position, d, 1)

    cp.draw(win)
    t_out.draw(win)
    t_in.draw(win)
    # h.draw(win, car.angle, car.position[0], car.position[1])
    car.draw(win)
    pg.display.flip()


# booleans to check if car is driving forward or backwards to fix steering
forward = True
backwards = False

check1 = ((147, 173),
          (239, 109),
          (385, 96),
          (505, 93),
          (619, 90),
          (745, 94),
          (833, 224),
          (747, 326),
          (730, 360),
          (740, 370),
          (820, 378),
          (942, 384),
          (1100, 403),
          (1170, 490),
          (1111, 647),
          (937, 674),
          (823, 682),
          (711, 681),
          (574, 679),
          (464, 677),
          (316, 675),
          (166, 611),
          (113, 478),
          (99, 377))
check2 = ((248, 260),
          (289, 222),
          (397, 217),
          (510, 210),
          (609, 206),
          (681, 217),
          (682, 223),
          (668, 241),
          (596, 361),
          (648, 473),
          (836, 494),
          (952, 501),
          (998, 516),
          (1007, 530),
          (1000, 544),
          (907, 555),
          (809, 562),
          (700, 561),
          (589, 559),
          (493, 557),
          (367, 552),
          (280, 516),
          (256, 451),
          (236, 376))
pos = 0
val = 0.3
track_out = [(100, 392),
(101, 249),
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
(133, 571),
(100, 392)]
track_in = [[236, 376],
                    [247, 260],
                    [289, 222],
                    [625, 205],
                    [681, 218],
                    [681, 229],
                    [636, 266],
                    [596, 341],
                    [596, 438],
                    [645, 473],
                    [726, 488],
                    [955, 501],
                    [980, 507],
                    [1005, 522],
                    [1008, 530],
                    [996, 550],
                    [786, 565],
                    [313, 548],
                    [267, 502],
            [236, 376]]

# making objects
t_out = track.Track(track_out)
t_in = track.Track(track_in)
cp = checkpoints.Checkpoints(check1[pos], check2[pos], 0.3)
car = car.Car()
# tog = line_gradient_calculator(track_out, track_in)

done = False
# main game loop
while not done:
    # set clock speed of game
    clock.tick(60)

    track = [t_out, t_in]

    for i in track:
        if pg.sprite.collide_mask(car, i):
            print('collide')
            pos = 0
            val = 0.3
            cp.__init__(check1[pos], check2[pos], val)
            car.__init__()

    if pg.sprite.collide_mask(car, cp):
        pos += 1
        if pos == len(check1):
            pos = 0
            val = 0.3
        cp.__init__(check1[pos], check2[pos], val)

    # to check if game window has been closed
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    # check for input
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        car.speed -= car.acceleration
        forward = True
        backwards = False
    if keys[pg.K_DOWN]:
        car.speed += car.deceleration
        forward = False
        backwards = True

    # car can only turn if the car is moving
    if keys[pg.K_RIGHT] and abs(car.speed) > 0.1 and forward:
        car.angle -= car.turn_speed
    if keys[pg.K_LEFT] and abs(car.speed) > 0.1 and forward:
        car.angle += car.turn_speed
    if keys[pg.K_RIGHT] and abs(car.speed) > 0.1 and backwards:
        car.angle += car.turn_speed
    if keys[pg.K_LEFT] and abs(car.speed) > 0.1 and backwards:
        car.angle -= car.turn_speed

    #  handbrake for car
    if keys[pg.K_SPACE]:
        if car.speed < 0:
            car.speed += 0.3
        if car.speed > 0:
            car.speed -= 0.3

    # simulate momentum
    if not done:
        if car.speed < 0:
            car.speed += 0.08
        if car.speed > 0:
            car.speed -= 0.08

    # setting speed to 0 if the car's absolute speed value is under 0.1 to be able to fully stop car
    if abs(car.speed) < 0.1:
        car.speed = 0

    # to check if car reached maximum speed
    if car.speed > car.max_forward_speed:
        car.speed = car.max_forward_speed
    if car.speed < car.max_reverse_speed:
        car.speed = car.max_reverse_speed

    # works out rotation of car
    x, y = car.position
    rad = car.angle * math.pi / 180
    x += car.speed * math.sin(rad)
    y += car.speed * math.cos(rad)
    car.position = (x, y)

    window()

pg.quit()
