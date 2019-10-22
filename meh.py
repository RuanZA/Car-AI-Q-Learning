import pygame as pg

pg.init()
image = pg.image.load("car.png")
clock = pg.time.Clock()
win = pg.display.set_mode((500, 500))

pg.display.set_caption("")


class Car(object):
    def __init__(self, x=250, y=250, angle=0.0, acceleration=1):
        self.x = x
        self.y = y
        self.angle = angle
        self.acceleration = acceleration

    def draw(self, w, rotated):
        rect = rotated.get_rect()
        self.angle += 1
        w.blit(rotated, (self.x - rect.width / 2.5, self.y - rect.height / 2.5))


def window():
    win.fill((0, 0, 0))
    image_rotated = pg.transform.rotate(image, s.angle)
    s.draw(win, image_rotated)
    print(s.angle)
    pg.display.update()


s = Car()
done = False
ppu = 53
while not done:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                s.angle += 1

    window()

pg.quit()