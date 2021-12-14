import pygame as pg
# from Game.Components import sansao

class Hero:
    def __init__(self, win, x, y):
        self.win = win
        self.x = 355
        self.y = y
        self.first = True

        self.thickness = 50
        self.heigt = 50
        self.vel = 15
        self.colour = "WHITE"

        self.monica_to_right = pg.image.load('Game\Components\media\monica_to_right.png')
        self.monica_to_right = pg.transform.scale(self.monica_to_right,(110,97))

        self.monica_to_left = pg.image.load('Game\Components\media\monica_to_left.png')
        self.monica_to_left = pg.transform.scale(self.monica_to_left,(110,97))

        self.default_monica = self.monica_to_right


    def control(self):
        keys = pg.key.get_pressed()
        if self.y <= 45:
            self.y = 600
        if self.y >= 624:
            self.y = 45
        if keys[pg.K_w]:
            self.y -= self.vel
        if keys[pg.K_s]:
            self.y += self.vel
    
    def draw(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]: 
            self.default_monica = self.monica_to_left
            self.x = 320

        elif keys[pg.K_d] :
            self.default_monica = self.monica_to_right
            self.x = 355

        self.win.blit(self.default_monica,(self.x,self.y))
            

