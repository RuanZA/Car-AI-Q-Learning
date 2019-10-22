import pygame as pg
import random

pg.init()
clock = pg.time.Clock()
win = pg.display.set_mode((500, 500))

pg.display.set_caption("snake")


class Snake(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 20
        self.width = 20
        self.vel = 20

    def draw(self, w):
        pg.draw.rect(w, (255, 255, 255), (self.x, self.y, self.width, self.height))


class Apple(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

    def draw(self, w):
        pg.draw.rect(w, (255, 0, 0), (self.x, self.y, self.width, self.height))


def window():
    win.fill((0, 0, 0))
    apple.draw(win)
    snake.draw(win)
    for s in snake_body:
        pg.draw.rect(win, (255, 255, 255), (s[0], s[1], 20, 20))
    pg.display.update()


def add(x, y):
    snake.draw(win, x, y)


def random_x():
    rand_x = random.randrange(5, 481)
    while not rand_x % 20 == 0:
        rand_x = random.randrange(5, 481)
    return rand_x


def random_y():
    rand_y = random.randrange(5, 481)
    while not rand_y % 20 == 0:
        rand_y = random.randrange(5, 481)
    return rand_y


snake = Snake(random_x(), random_y())
apple = Apple(random_x(), random_y())
snake_body = [[snake.x, snake.y]]
d = random.choice(["left", "right", "up", "down"])
apple.draw(win)
apple_eaten = False
run = True
while run:
    clock.tick(7)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    head_x = snake_body[0][0]
    head_y = snake_body[0][1]

    if (head_x == apple.x) and (head_y == apple.y):
        apple.x = random_x()
        apple.y = random_y()
        apple_eaten = True

    if keys[pg.K_LEFT] and not d == "right":
        d = "left"
    elif keys[pg.K_RIGHT] and not d == "left":
        d = "right"
    elif keys[pg.K_UP] and not d == "down":
        d = "up"
    elif keys[pg.K_DOWN] and not d == "up":
        d = "down"

    if d == "left" and snake.x > 0:
        snake.x -= snake.vel
    if d == "right" and snake.x < 480:
        snake.x += snake.vel
    if d == "up" and snake.y > 0:
        snake.y -= snake.vel
    if d == "down" and snake.y < 480:
        snake.y += snake.vel

    if [snake.x, snake.y] in snake_body[1:]:
        print("lost")
        print(len(snake_body))
        run = False

    newPart = [snake.x, snake.y]

    snake_body.insert(0, newPart)
    snake_body.pop()

    if apple_eaten:
        snake_body.insert(1, [head_x, head_y])
        # pg.draw.rect(win, (255, 255, 255), (snake_body[-1][0], snake_body[-1][1], 20, 20))
        apple_eaten = False

    window()

pg.quit()
