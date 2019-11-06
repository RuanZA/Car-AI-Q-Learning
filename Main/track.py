"""
Track class

This is where the track's "hitbox" is going to be drawn
"""
import pygame as pg


class Track(pg.sprite.Sprite):
    def __init__(self, points):
        pg.sprite.Sprite.__init__(self)
        self.position = (0, 0)
        self.points = points
        self.image = pg.Surface([1280, 720], pg.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pg.draw.lines(self.image, (255, 255, 255), True, self.points, 1)
        # self.image = self.image.convert_alpha(self.image)
        self.rect = self.image.get_rect()
        # self.image.fill((0, 255, 0))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, w):
        w.blit(self.image, self.position)
