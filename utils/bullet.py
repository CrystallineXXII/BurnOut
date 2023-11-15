import pygame as pg
from pygame.math import Vector2

from .particle import Particle
from .blocks import Wall_Grp


def make_Explosion(pos, color=None):
    for i in range(10):
        Particle(pos.copy(), i, color=color)


Bullet_Grp = pg.sprite.Group()


class Bullet(pg.sprite.Sprite):
    def __init__(self, pos: Vector2, direction: Vector2):
        super().__init__(Bullet_Grp)
        self.pos = pos + direction * 300
        self.startpos = pos.copy()
        self.dir = direction

        self.trail_points = []

    def update(self, screen, deltatime, *, campos):
        self.pos += self.dir * 1000 * deltatime
        self.trail_points.append(self.pos.copy())
        self.trail_points = self.trail_points[-20:]

        if len(self.trail_points) > 2:
            pg.draw.lines(screen, "#00ffc8", False, [i - campos for i in self.trail_points])

        pg.draw.circle(screen, "#00ffc8", self.pos - campos, 3)


class Laser(pg.sprite.Sprite):
    def __init__(self, pos: Vector2, direction: Vector2):
        super().__init__(Bullet_Grp)
        self.tpos = pos + direction * 300
        self.startpos = pos.copy()
        self.dir = direction

        self.lifetime = 0

    def update(self, screen, deltatime, *, campos):

        endpos = self.startpos.copy()
        for i in range(60):
            out = False
            endpos += self.dir * 5 
            for wall in Wall_Grp:
                if wall.rect.collidepoint(endpos + campos):
                    wall.onfire()
                    out = True

            if out:
                break
        if self.lifetime <= 0.1:
            pg.draw.line(
                screen,
                "#00ffc8",
                self.startpos ,
                endpos ,
            )
            self.lifetime += deltatime
        else:
            self.lifetime = 0

            self.kill()
            make_Explosion(endpos + campos)
