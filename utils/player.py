import pygame as pg
from pygame.math import Vector2
from math import radians
from .bullet import Bullet, Laser


def draw_polygon(pos, n, radius, angle=0):
    radialVec = Vector2(1, 0).rotate(angle) * radius
    stepAngle = 360 / n

    listOfPoints = []
    for i in range(n):
        listOfPoints.append(pos + radialVec.rotate(stepAngle * i))

    return listOfPoints


class Player:
    def __init__(self, pos: Vector2):
        self.pos = pos
        self.shoot_timer = 0

    def get_input(self, deltatime):
        keys = pg.key.get_pressed()
        inputvec = Vector2(0, 0)

        if keys[pg.K_w]:
            inputvec += Vector2(0, -1)
        if keys[pg.K_s]:
            inputvec += Vector2(0, 1)
        if keys[pg.K_a]:
            inputvec += Vector2(-1, 0)
        if keys[pg.K_d]:
            inputvec += Vector2(1, 0)

        return inputvec.normalize() if inputvec.magnitude() > 0 else inputvec

    def shoot(self):
        if self.shoot_timer == 0:
            self.shoot_timer = 0
            Laser(
                self.pos.copy(),
                (Vector2(pg.mouse.get_pos()) - self.pos).normalize(),
            )
            # print("shot")
        # print(self.shoot_timer)

    def update(self, screen, deltatime):
        inputvec = self.get_input(deltatime)

        self.pos += inputvec * 250 * deltatime

        pg.draw.circle(screen, "red", self.pos, 10)
        pg.draw.circle(screen, "#555555", self.pos, 310, 1)

        ang = (Vector2(pg.mouse.get_pos()) - self.pos).angle_to(Vector2(1, 0))

        pg.draw.polygon(
            screen,
            "red",
            draw_polygon(self.pos + Vector2(15, 0).rotate(-ang), 3, 5, -ang),
        )

        pg.draw.arc(
            screen,
            "#0487df",
            pg.Rect(self.pos.x - 15, self.pos.y - 15, 30, 30),
            radians(ang + 40),
            radians(ang - 40),
        )
