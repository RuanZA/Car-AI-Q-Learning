"""
Car class

This is where the car is drawn and given values
"""
import pygame as pg


class Car(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.x = 170
        self.y = 320
        self.position = (self.x, self.y)
        self.angle = 0.0
        self.speed = 0
        self.deceleration = 0.8
        self.acceleration = 0.5

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
