"""
Hit box class

This is where the hit box is calculated based on the car's position
"""
import math
import pygame as pg


class Hitbox(pg.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pg.sprite.Sprite.__init__(self)
        self.pos = (x, y)
        self.angle = 0
        self.image = pg.Surface([201, 201], pg.SRCALPHA, 32)
        # self.image = pg.Surface([201, 201])
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        i = 0
        while i <= 315:
            x = self.rect.center[0] + math.cos(math.radians(-self.angle + i)) * 100
            y = self.rect.center[1] + math.sin(math.radians(-self.angle + i)) * 100
            pg.draw.line(self.image, (0, 255, 0), self.rect.center, (x, y), 2)
            i += 45
        self.rotated = pg.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()

        self.mask = pg.mask.from_surface(self.rotated)

    def draw(self, w, a, x, y):

        self.rotated = pg.transform.rotate(self.image, a)
        self.rect = self.rotated.get_rect()

        self.rect.center = (x, y)

        w.blit(self.rotated, self.rect)
