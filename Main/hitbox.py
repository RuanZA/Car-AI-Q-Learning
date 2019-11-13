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
        x = self.rect.center[0] + math.cos(math.radians(-self.angle + 0)) * 150
        y = self.rect.center[1] + math.sin(math.radians(-self.angle + 0)) * 150

    def draw(self, w, a, x, y):

