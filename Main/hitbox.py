"""
Hitbox class

This is where the hitbox is calculated based on the car's position
"""
import math
import pygame as pg


class Hitbox(pg.sprite.Sprite):
    def draw(self, w, a, x, y):
        """
        this code gets the position of the car and draws a box from that point

        then shifts the box to fit over the car
        """

        car_middle = (x, y)
        angle = 116.3 # place holder
        x = car_middle[0] + math.cos(math.radians(-a + -angle)) * math.sqrt(math.pow(53, 2) + math.pow(27, 2)) / 2
        y = car_middle[1] + math.sin(math.radians(-a + -angle)) * math.sqrt(math.pow(53, 2) + math.pow(27, 2)) / 2

        origin = (x, y)
        x = origin[0] + math.cos(math.radians(-a + 90)) * 53
        y = origin[1] + math.sin(math.radians(-a + 90)) * 53

        x2 = x + math.cos(math.radians(-a + 0)) * 27
        y2 = y + math.sin(math.radians(-a + 0)) * 27

        x3 = x2 + math.cos(math.radians(-a + -90)) * 53
        y3 = y2 + math.sin(math.radians(-a + -90)) * 53

        x4 = x3 + math.cos(math.radians(-a + -180)) * 27
        y4 = y3 + math.sin(math.radians(-a + -180)) * 27

        pg.draw.lines(w, (0, 255, 0), True, ((x, y), (x2, y2), (x3, y3), (x4, y4)), 1)

        x = car_middle[0] + math.cos(math.radians(-a + 0)) * 100
        y = car_middle[1] + math.sin(math.radians(-a + 0)) * 100

        x2 = car_middle[0] + math.cos(math.radians(-a + 45)) * 100
        y2 = car_middle[1] + math.sin(math.radians(-a + 45)) * 100

        x3 = car_middle[0] + math.cos(math.radians(-a + 90)) * 100
        y3 = car_middle[1] + math.sin(math.radians(-a + 90)) * 100

        x4 = car_middle[0] + math.cos(math.radians(-a + 135)) * 100
        y4 = car_middle[1] + math.sin(math.radians(-a + 135)) * 100

        x5 = car_middle[0] + math.cos(math.radians(-a + 180)) * 100
        y5 = car_middle[1] + math.sin(math.radians(-a + 180)) * 100

        x6 = car_middle[0] + math.cos(math.radians(-a + 225)) * 100
        y6 = car_middle[1] + math.sin(math.radians(-a + 225)) * 100

        x7 = car_middle[0] + math.cos(math.radians(-a + 270)) * 100
        y7 = car_middle[1] + math.sin(math.radians(-a + 270)) * 100

        x8 = car_middle[0] + math.cos(math.radians(-a + 315)) * 100
        y8 = car_middle[1] + math.sin(math.radians(-a + 315)) * 100

        pg.draw.line(w, (0, 255, 0), car_middle, (x, y), 1)

        pg.draw.line(w, (0, 255, 0), car_middle, (x2, y2), 1)

        pg.draw.line(w, (0, 255, 0), car_middle, (x3, y3), 1)

        pg.draw.line(w, (0, 255, 0), car_middle, (x4, y4), 1)

        pg.draw.line(w, (0, 255, 0), car_middle, (x5, y5), 1)

        pg.draw.line(w, (0, 255, 0), car_middle, (x6, y6), 1)

        pg.draw.line(w, (0, 255, 0), car_middle, (x7, y7), 1)

        pg.draw.line(w, (0, 255, 0), car_middle, (x8, y8), 1)
