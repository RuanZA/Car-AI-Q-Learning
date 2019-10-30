"""
Hitbox class

This is where the hitbox is calculated based on the car's position
"""
import math
import pygame as pg


class Hitbox(object):
    def draw(self, w, a, x, y):
        """
        this code gets the position of the car and draws a box from that point

        then shifts the box to fit over the car
        """
        origin = (x, y)
        angle = 116.3 # place holder
        x = origin[0] + math.cos(math.radians(-a + -angle)) * math.sqrt(math.pow(53, 2) + math.pow(27, 2)) / 2
        y = origin[1] + math.sin(math.radians(-a + -angle)) * math.sqrt(math.pow(53, 2) + math.pow(27, 2)) / 2

        origin = (x, y)
        x = origin[0] + math.cos(math.radians(-a + 90)) * 53
        y = origin[1] + math.sin(math.radians(-a + 90)) * 53

        x2 = x + math.cos(math.radians(-a + 0)) * 27
        y2 = y + math.sin(math.radians(-a + 0)) * 27

        x3 = x2 + math.cos(math.radians(-a + -90)) * 53
        y3 = y2 + math.sin(math.radians(-a + -90)) * 53

        pg.draw.line(w, (0, 255, 0), origin, (x, y), 1)
        pg.draw.line(w, (0, 255, 0), (x, y), (x2, y2), 1)
        pg.draw.line(w, (0, 255, 0), (x2, y2), (x3, y3), 1)
        pg.draw.line(w, (0, 255, 0), (x3, y3), origin, 1)
