"""
Checkpoints class

This is where the checkpoints are being draw

Checkpoints will be guidelines for the car to be able to go around the course
"""
import pygame as pg


class Checkpoints(object):
    def __init__(self, point_a, point_b, val):
        pg.sprite.Sprite.__init__(self)
        self.position = (0, 0)
        self.value = val
        self.begin = point_a
        self.end = point_b
        self.image = pg.Surface([1280, 720], pg.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pg.draw.line(self.image, (255, 0, 0), self.begin, self.end, 1)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, w):
        w.blit(self.image, self.position)
