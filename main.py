import pygame as pg
from pygame.math import Vector2
from time import time

import utils

pg.init()
screen = pg.display.set_mode((1600, 1000))


def make_Explosion(pos):
    for i in range(36):
        utils.Particle(pos.copy(),Vector2(1,0).rotate(10*i))


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
        pg.display.update()

        deltatime = time() - strTime

        for bullet in utils.Bullet_Grp.copy():
            if (player.pos - bullet.pos).magnitude() > 300:
                make_Explosion(bullet.pos)
                bullet.kill()
                break

main()