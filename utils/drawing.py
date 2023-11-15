import pygame as pg
from pygame.math import Vector2

def fade_to(surface, color, duration):
    surf = pg.Surface((1200, 750))
    surf.fill(color)
    for i in range(60):
        surf.set_alpha(int(17))
        surface.blit(surf, (0, 0))
        pg.display.flip()
        pg.time.delay(int(duration * 1000 / 60))