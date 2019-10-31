"""
Track class

This is where the track's "hitbox" is going to be drawn
"""
import pygame as pg

class Track(pg.sprite.Sprite):
    def __init__(self):
        pass

    def draw(self, w, c):
        pg.draw.lines(w, (0, 0, 0), True, c, 1)
