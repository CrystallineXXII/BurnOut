from typing import Any
import pygame as pg
from pygame.math import Vector2
from random import randint

from .particle import Particle

def make_Explosion(pos):
    for i in range(10):
        Particle(pos.copy(), i)

Wall_Grp = pg.sprite.Group()

class Wall(pg.sprite.Sprite):
    def __init__(self, pos: Vector2):
        super().__init__(Wall_Grp)
        self.pos = pos
        self.rect = pg.Rect(pos.x, pos.y, 50, 50)
        self.image = pg.Surface((50, 50))
        self.image.fill("#ffffff")

        self.fireCounter = 0
        self.c1 = 0
        
    def onfire(self):
        self.fireCounter = 5
    def update(self,screen,deltatime):
        if self.fireCounter > 0:
            self.fireCounter -= deltatime
            self.c1 += deltatime * 100
            if self.c1 > 10 :
                make_Explosion(self.pos  + Vector2(25,25) + Vector2(randint(-20,20),randint(-20,20)))
                self.c1 = 0
        screen.blit(self.image, self.rect)