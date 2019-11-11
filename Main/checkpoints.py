"""
Checkpoints class

This is where the checkpoints are being draw

Checkpoints will be guidelies for the car to be able to go around the course
"""
import pygame as pg


class Checkpoints(object):
    def __init__(self, points):
        self.position = (0, 0)
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([1280, 720], pg.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        i = 0
        while i < len(points):
            pg.draw.line(self.image, (255, 0, 0), points[i], points[i+1], 10)
            i += 2
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, w):
        w.blit(self.image, self.position)
