import pygame as pg
pg.init()

clock = pg.time.Clock()

win = pg.display.set_mode((500, 700))

pg.display.set_caption("Flappy Bird")


class Bird(object):
    def __init__(self, x=50, y=350, gravity=1):
        self.x = x
        self.y = y
        self.gravity = gravity

    def draw(self, w):
        pg.draw.rect(w, (133, 200, 0), (self.x, self.y, 20, 20))


def window():
    win.fill((0, 0, 0))
    bird.draw(win)
    pg.display.update()


gravity = 0.001
velocity = 0
bird = Bird()
run = True
keyDown = False
while run:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bird.gravity = 0
                for i in range(4):
                    bird.y -= 20
            bird.gravity = 1
    bird.y += bird.gravity
    if bird.gravity < 10:
        bird.gravity = bird.gravity * 1.08

    window()

pg.quit()
