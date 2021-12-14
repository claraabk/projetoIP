import pygame as pg
import os


class Hero:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y
        self.vel = 15

    def control(self):
        keys = pg.key.get_pressed()
        if self.y <= -50:
            self.y = 529
        if self.y >= 624:
            self.y = 1
        if keys[pg.K_w]:
            self.y -= self.vel
        if keys[pg.K_s]:
            self.y += self.vel

    def draw(self):
        x = pg.key.get_pressed()
        if x[pg.K_a]:
            monica = pg.image.load(os.path.join(os.path.dirname(__file__), "img/arma_esquerda.png"))
        elif x[pg.K_d]:
            monica = pg.image.load(os.path.join(os.path.dirname(__file__), "img/arma.png"))
        else:
            monica = pg.image.load(os.path.join(os.path.dirname(__file__), "img/arma_esquerda.png"))
        self.win.blit(monica, (self.x, self.y))


class Bullet:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

    def draw_right(self):
        sansao = pg.image.load(os.path.join(os.path.dirname(__file__), "img/sansao.png"))
        self.win.blit(sansao, (self.x+50, self.y+10))
        self.x += 20

    def draw_left(self):
        sansao = pg.image.load(os.path.join(os.path.dirname(__file__), "img/sansao.png"))
        self.win.blit(sansao, (self.x-10, self.y+10))
        self.x -= 20
