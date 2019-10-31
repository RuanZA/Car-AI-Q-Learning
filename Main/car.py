"""
Car class

This is where the car is drawn and given values
"""
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
        self.max_reverse_speed = -9

    def draw(self, w, i):
        # rotates car
        rotated = pg.transform.rotate(i, self.angle)
        rect = rotated.get_rect()
        # sets car's position to center of image
        rect.center = self.position
        print(self.angle)
        print(self.position)
        print(self.speed)
        # displays image on window
        w.blit(rotated, rect)
        pg.display.flip()
