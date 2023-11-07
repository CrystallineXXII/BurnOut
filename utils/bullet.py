import pygame as pg
from pygame.math import Vector2

from .particle import Particle


def make_Explosion(pos):
    for i in range(10):
        Particle(pos.copy(), i)


Bullet_Grp = pg.sprite.Group()


class Bullet(pg.sprite.Sprite):
    def __init__(self, pos: Vector2, direction: Vector2):
        super().__init__(Bullet_Grp)
        self.pos = pos + direction * 300
        self.startpos = pos.copy()
        self.dir = direction

        self.trail_points = []

    def update(self, screen, deltatime):
        self.pos += self.dir * 1000 * deltatime
        self.trail_points.append(self.pos.copy())
        self.trail_points = self.trail_points[-20:]

        if len(self.trail_points) > 2:
            pg.draw.lines(screen, "#00ffc8", False, self.trail_points)

        pg.draw.circle(screen, "#00ffc8", self.pos, 3)


class Laser(pg.sprite.Sprite):
    def __init__(self, pos: Vector2, direction: Vector2):
        super().__init__(Bullet_Grp)
        self.tpos = pos + direction * 300
        self.startpos = pos.copy()
        self.dir = direction

        self.lifetime = 0

    def update(self, screen, deltatime):
        if self.lifetime <= 0.1:
            pg.draw.line(
                screen,
                "#00ffc8",
                self.startpos,
                self.tpos,
            )
            self.lifetime += deltatime
        else:
            self.lifetime = 0

            self.kill()
            make_Explosion(self.tpos)
