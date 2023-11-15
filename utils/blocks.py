
import pygame as pg
from pygame.math import Vector2
from random import randint

from .particle import Particle

def make_Explosion(pos,color = None):
    for i in range(10):
        Particle(pos.copy(), i, color = color)

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
    def update(self,screen,deltatime,*,campos):
        if self.fireCounter > 0:
            self.fireCounter -= deltatime
            self.c1 += deltatime * 100
            if self.c1 > 10 :
                make_Explosion(self.pos  + Vector2(25,25) + Vector2(randint(-20,20),randint(-20,20)))
                self.c1 = 0

        rect = pg.Rect(self.pos.x - campos.x, self.pos.y - campos.y, 50, 50)

        screen.blit(self.image, rect)

Torch_Grp = pg.sprite.Group()

#shades of light blue
torch_colors = ["#00ffc8","#00e0ff","#00b4ff","#0099ff","#0077ff","#005aff","#0040ff","#0026ff","#0010ff","#0000ff"]

class Torch(pg.sprite.Sprite):
    def __init__(self,pos:Vector2):
        super().__init__(Torch_Grp)

        self.pos = pos
        self.c1 = 0

    def update(self,screen,deltatime,*,campos):

        pg.draw.circle(screen,'#583f00',self.pos - campos,20)

        if self.c1 > 20 :
            make_Explosion(self.pos + Vector2(randint(-10,20),randint(-10,10)),color = torch_colors)
            self.c1 = 0
        else:
            self.c1 += deltatime * 100

        