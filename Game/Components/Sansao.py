import pygame as pg

class Bullet:
    def __init__(self, x, y):
        self.image = pg.Surface((800,600))
        self.x = x
        self.y = y
        self.rect= self.image.get_rect(center = (x, y))

    def update(self):
        self.rect += 5