from .particle import Particle, Particle_Grp
from .player import Player, draw_polygon
from .txt_button import TxtButton

from .drawing import fade_to


from pygame.math import Vector2
import pygame as pg

def make_Explosion(pos):
    for i in range(36):
        Particle(pos.copy(), Vector2(1, 0).rotate(10 * i))

from .bullet import Bullet, Laser, Bullet_Grp
from .blocks import Wall, Wall_Grp, Torch, Torch_Grp

pg.font.init()

smol_font = pg.font.Font("Assets/Fonts/Raleway.ttf", 15)
big_font = pg.font.Font("Assets/Fonts/Raleway.ttf", 40)
huge_font = pg.font.Font("Assets/Fonts/Raleway.ttf", 100)

def debug(display_surf, text):
    text = smol_font.render(text, True, "#eeeeee")
    display_surf.blit(text, (0, 0))


def text(screen, text, pos, font="smol"):
    match font:
        case "smol":
            text = smol_font.render(text, True, "#ffffff")
        case "big":
            text = big_font.render(text, True, "#ffffff")
        case "huge":
            text = huge_font.render(text, True, "#ffffff")
        case _:
            raise Exception("Invalid font")

    screen.blit(text, text.get_rect(center=pos))


def image(screen, img, pos, scale=1):
    img = pg.transform.rotozoom(img, 0, scale)
    screen.blit(img, img.get_rect(center=pos))
