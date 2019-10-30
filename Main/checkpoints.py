"""
Checkpoints class

This is where the checkpoints are being draw

Checkpoints will be guidelies for the car to be able to go around the course
"""
import pygame as pg


class Checkpoints(object):
    def __init__(self):
        pass

    def draw(self, w, point_a, point_b):

        pg.draw.line(w, (255, 0, 0), point_a, point_b, 1)
