import pygame as pg
from pygame.math import Vector2
from random import randint

Particle_Grp = pg.sprite.Group()

class Particle(pg.sprite.Sprite):
    def __init__(self, pos: Vector2, i: int):
        super().__init__(Particle_Grp)

        self.pos = pos.copy() + Vector2(randint(-15, 15), randint(-15, 15))
        self.i_val = i
        self.alive_time = 0
        self.explosion_radius = randint(10, 40-self.i_val)
        self.explosion_color = ["#f9f900", "#ff9d00", "#ff6a00"][randint(0, 2)]

        self.trail_points = []

    def update(self, screen, deltatime):
        self.alive_time += deltatime
        radius = self.explosion_radius * (self.alive_time)
        if self.alive_time > .5:
            radius = self.explosion_radius * (1-self.alive_time)
        if self.alive_time > 1:
            self.kill()

        pg.draw.circle(screen, self.explosion_color, self.pos, radius)
