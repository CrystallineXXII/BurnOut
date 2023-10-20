import pygame as pg
from pygame.math import Vector2
from time import time
from math import radians,degrees

pg.init()
screen = pg.display.set_mode((800,500))

class Player:
    def __init__(self,pos:Vector2):
        self.pos = pos
        self.shoot_timer = 0
        
    def get_input(self,deltatime):
        keys = pg.key.get_pressed()
        inputvec = Vector2(0,0)

        if keys[pg.K_w]:
            inputvec += Vector2(0,-1)
        if keys[pg.K_s]:
            inputvec += Vector2(0,1)
        if keys[pg.K_a]:
            inputvec += Vector2(-1,0)
        if keys[pg.K_d]:
            inputvec += Vector2(1,0)

        if pg.mouse.get_pressed()[0]:
            self.shoot_timer += deltatime
            if self.shoot_timer >= 0.1:
                self.shoot_timer = 0
                Bullet(self.pos.copy(),(Vector2(pg.mouse.get_pos()) - self.pos).normalize())
                #print("shot")
            #print(self.shoot_timer)

        return inputvec.normalize() if inputvec.magnitude() > 0 else inputvec

    def update(self,deltatime):
        inputvec = self.get_input(deltatime)

        self.pos += inputvec *250* deltatime

        pg.draw.circle(screen,"red",self.pos,10)

        ang = (Vector2(pg.mouse.get_pos()) - self.pos ).angle_to(Vector2(1,0))

        pg.draw.arc(screen,"#0487df",pg.Rect(self.pos.x - 15,self.pos.y - 15,30,30),radians(ang-30),radians(ang+30))



Bullet_Grp = pg.sprite.Group()
class Bullet(pg.sprite.Sprite):
    def __init__(self,pos:Vector2,direction:Vector2):
        super().__init__(Bullet_Grp)
        self.pos = pos
        self.dir = direction
    
    def update(self,deltatime):
        self.pos += self.dir * 1000 * deltatime
        
        pg.draw.circle(screen,'#fbff00',self.pos,3)

def main():
    deltatime = 1/400
    player = Player(Vector2(400,250))
    while True:
        strTime = time()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        screen.fill("#272727")
        player.update(deltatime)
        Bullet_Grp.update(deltatime)
        pg.display.update()

        deltatime = time() - strTime

main()
        