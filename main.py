import pygame as pg
from pygame.math import Vector2
from time import time

import utils

pg.init()
screen = pg.display.set_mode((1600, 1000))





def main():
    deltatime = 1
    player = utils.Player(Vector2(400, 250))
    while True:
        strTime = time()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        screen.fill("#272727")
        utils.Bullet_Grp.update(screen,deltatime)
        utils.Particle_Grp.update(screen,deltatime)
        player.update(screen,deltatime)
        utils.debug(screen,f"FPS: {1/deltatime:.0f}")
        pg.display.update()

        deltatime = time() - strTime

        for bullet in utils.Bullet_Grp.copy():
            if (player.pos - bullet.pos).magnitude() > 300:
                utils.make_Explosion(bullet.pos)
                bullet.kill()

def menu():
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return main,()

        screen.fill("#272727")
        pg.draw.rect(screen,"#00ffc8",pg.Rect(20,20,1560,960),5)
        utils.text(screen,"BurnOut",Vector2(350,150), font="huge")
        pg.display.update()

if __name__ == "__main__":
    func = menu
    values = ()

    while True: 
        func, values = func(*values)