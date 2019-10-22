import os
from math import sin, radians, degrees, copysign
import pygame as pg
from pygame.math import Vector2



class Car(pg.sprite.Sprite):
    def __init__(self, x, y, angle=0.0, length=4, max_steering=100, max_acceleration=1.0):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 20
        self.brake_deceleration = 200
        self.free_deceleration = 2

        self.acceleration = 3.0
        self.steering = 0.0

    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)

        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Car AI")
        win_width = 1000
        win_height = 500
        self.screen = pg.display.set_mode((win_width, win_height))
        self.clock = pg.time.Clock()
        self.ticks = 60
        self.exit = False

    def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "car.png")
        car_image = pg.image.load(image_path)
        car = Car(0, 0)
        ppu = 53

        while not self.exit:
            dt = self.clock.get_time() / 1000

            # Event queue
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.exit = True

            # User input
            pressed = pg.key.get_pressed()

            if pressed[pg.K_UP]:
                if car.velocity.x < 0:
                    car.acceleration = car.brake_deceleration
                else:
                    car.acceleration += 1 * dt
            elif pressed[pg.K_DOWN]:
                if car.velocity.x > 0:
                    car.acceleration = -car.brake_deceleration
                else:
                    car.acceleration -= 1 * dt
            elif pressed[pg.K_SPACE]:
                if car.velocity.x != 0:
                    car.acceleration = copysign(car.max_acceleration, -car.velocity.x)
            else:
                car.acceleration = 0
            car.acceleration = max(-car.max_acceleration, min(car.acceleration, car.max_acceleration))

            if pressed[pg.K_RIGHT]:
                car.steering -= 30 * dt
            elif pressed[pg.K_LEFT]:
                car.steering += 30 * dt
            else:
                car.steering = 0
            car.steering = max(-car.max_steering, min(car.steering, car.max_steering))

            # Logic
            car.update(dt)

            # Drawing
            self.screen.fill((0, 0, 0))
            rotated = pg.transform.rotate(car_image, car.angle)
            rect = rotated.get_rect()
            self.screen.blit(rotated, car.position * ppu - (rect.width / 2, rect.height / 2))

        pg.quit()


if __name__ == '__main__':
    game = Game()
    game.run()




