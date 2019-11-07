"""
Car class

This is where the car is drawn and given values
"""
import pygame as pg


class Car(pg.sprite.Sprite):
    def __init__(self, x=170, y=320, angle=0.0, speed=0, deceleration=1, acceleration=1, *groups):
        super().__init__(*groups)
        self.position = (x, y)
        self.angle = angle
        self.speed = speed
        self.deceleration = deceleration
        self.acceleration = acceleration
        self.turn_speed = 5
        self.max_forward_speed = 5
        self.max_reverse_speed = -9
        self.image = pg.image.load("car.png")
        self.rotated = pg.transform.rotate(self.image, self.angle)
        self.rect = self.rotated.get_rect()
        self.mask = pg.mask.from_surface(self.rotated)

    def draw(self, w):
        # rotates car
        self.rotated = pg.transform.rotate(self.image, self.angle)
        self.rect = self.rotated.get_rect()

        # sets car's position to center of image
        self.rect.center = self.position

        # displays image on window
        w.blit(self.rotated, self.rect)
        self.mask = pg.mask.from_surface(self.rotated)
        pg.display.flip()
