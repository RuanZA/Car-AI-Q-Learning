import pygame as pg


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

    def draw(self, w, i):
        rotated = pg.transform.rotate(i, self.angle)
        rect = rotated.get_rect()
        rect.center = self.position
        print(self.angle)
        print(self.position)
        print(self.speed)
        w.blit(rotated, rect)
        pg.display.flip()
