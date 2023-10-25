import pygame as pg
from pygame.math import Vector2

Bullet_Grp = pg.sprite.Group()

class Bullet(pg.sprite.Sprite):
    def __init__(self, pos: Vector2, direction: Vector2):
        super().__init__(Bullet_Grp)
        self.pos = pos
        self.startpos = pos.copy()
        self.dir = direction

        self.trail_points = []

    def update(self,screen, deltatime):
        self.pos += self.dir * 1000 * deltatime
        self.trail_points.append(self.pos.copy())
        self.trail_points = self.trail_points[-20:]



        if len(self.trail_points) > 2:
            pg.draw.lines(screen,"#00ffc8",False,self.trail_points)


        pg.draw.circle(screen, "#00ffc8", self.pos, 3)

