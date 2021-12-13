import pygame as pg

class Hero:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

        self.thickness = 50
        self.heigt = 50
        self.vel = 15
        self.colour = "WHITE"

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
        pg.draw.rect(self.win, self.colour, (self.x, self.y, self.thickness, self.heigt))