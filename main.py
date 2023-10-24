import pygame as pg
from pygame.math import Vector2
from time import time
from math import radians, degrees

pg.init()
screen = pg.display.set_mode((1600, 1000))


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

        if pg.mouse.get_pressed()[0]:
            self.shoot_timer += deltatime
            if self.shoot_timer >= 0.1:
                self.shoot_timer = 0
                Bullet(
                    self.pos.copy(),
                    (Vector2(pg.mouse.get_pos()) - self.pos).normalize(),
                )
                # print("shot")
            # print(self.shoot_timer)

        return inputvec.normalize() if inputvec.magnitude() > 0 else inputvec

    def update(self, deltatime):
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


Bullet_Grp = pg.sprite.Group()


class Bullet(pg.sprite.Sprite):
    def __init__(self, pos: Vector2, direction: Vector2):
        super().__init__(Bullet_Grp)
        self.pos = pos
        self.startpos = pos.copy()
        self.dir = direction

    def update(self, deltatime):
        self.pos += self.dir * 1000 * deltatime

        pg.draw.circle(screen, "#0487df", self.pos, 3)


def main():
    deltatime = 1 / 400
    player = Player(Vector2(400, 250))
    while True:
        strTime = time()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        screen.fill("#272727")
        Bullet_Grp.update(deltatime)
        player.update(deltatime)
        pg.display.update()

        deltatime = time() - strTime

        for bullet in Bullet_Grp.copy():
            if (bullet.startpos - bullet.pos).magnitude() > 300:
                bullet.kill()


main()
