import pygame as pg
from pygame.math import Vector2
from time import time

import utils

pg.init()
screen = pg.display.set_mode((1200, 750))
pg.display.set_caption("BurnOut")


def main():
    cover_rect = pg.Surface((1200, 750))
    cover_rect.fill("#000000")
    cover_rect.set_colorkey("white")
    cover_rect.set_alpha(250)

    campos = Vector2(0, 0)

    c = pg.time.Clock()
    deltatime = 1
    player = utils.Player(Vector2(400, 250))

    for i in range(10):
        utils.Wall(Vector2(100 + 100 * i, 100))

    for i in range(4):
        utils.Torch(Vector2(100 + 200 * i, 500))

    while True:
        strTime = time()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        if pg.mouse.get_pressed()[0]:
                player.shoot(deltatime,campos=campos)

        screen.fill("#272727")
        cover_rect.fill("#101010")

        pg.draw.circle(cover_rect, "#ffffff", player.pos, 350)

        for i in utils.Particle_Grp.copy():
            pg.draw.circle(cover_rect, "#ffffff", i.pos - campos, 40)

        for i in utils.Torch_Grp.copy():
            pg.draw.circle(cover_rect, "#ffffff", i.pos - campos, 500)
            
        utils.Bullet_Grp.update(screen, deltatime, campos = campos)

        player.update(screen, deltatime, campos = campos)


        utils.Wall_Grp.update(screen, deltatime, campos = campos)
        utils.Torch_Grp.update(screen, deltatime, campos = campos)
        utils.Particle_Grp.update(screen, deltatime, campos = campos)

        screen.blit(cover_rect, (0, 0))

        utils.debug(screen, f"FPS: {1/deltatime:.0f} | cam: {campos} | player: {player.pos}")
        pg.display.update()

        for bullet in utils.Bullet_Grp.copy():
            if isinstance(bullet, utils.Bullet):
                if (player.pos - bullet.pos).magnitude() > 300:
                    utils.make_Explosion(bullet.pos)
                    bullet.kill()



        c.tick(60)
        deltatime = time() - strTime


def menu():
    logo = pg.image.load("Assets/Images/title.png")

    y = 300
    x = 950
    play_button = utils.TxtButton(x, y, "PLAY GAME", "#ffffff", utils.big_font)
    settings_button = utils.TxtButton(x, y + 100, "SETTINGS", "#ffffff", utils.big_font)
    quit_button = utils.TxtButton(x, y + 200, "QUIT", "#ffffff", utils.big_font)

    while True:
        mpos = (0, 0)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mpos = pg.mouse.get_pos()

        screen.fill("#272727")
        # pg.draw.rect(screen,"#00ffc8",pg.Rect(20,20,1560,960),5)
        utils.image(screen, logo, Vector2(400, 375), scale=0.6)

        if play_button.update(screen, mpos):
            utils.fade_to(screen, "#272727", 0.01)
            return main, ()
        if settings_button.update(screen, mpos):
            utils.fade_to(screen, "#272727", 0.25)
            return menu, ()
        if quit_button.update(screen, mpos):
            pg.quit()
            exit()
        pg.display.update()

def intro():

    logo = pg.image.load("Assets/Images/logo.png")
    logo = pg.transform.rotozoom(logo, 0, 0.1)
    rect = logo.get_rect(center=(600, 375))
   
    clock = pg.time.Clock()

    mode = "in"
    c = 0; s = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        screen.fill("#272727")
        logo.set_alpha(c)
        screen.blit(logo, rect)
        pg.display.update()
        pg.time.delay(2)


        if c > 255 and mode == "in":
            mode = "stay"
        if s > 60 and mode == "stay":
            mode = "out"

        if mode == "in":
            c += 8
        elif mode == "stay":
            s += 1
        elif mode == "out":
            c -= 8

        if mode == "out" and c < 0:
            utils.fade_to(screen, "#272727", 0.25)
            return menu, ()


        clock.tick(60)
        print(c)

if __name__ == "__main__":
    func = intro
    values = ()

    while True:
        func, values = func(*values)
