import pygame as pg


class Hero():
    def __init__(self, win, y):
        self.win = win
        self.x = 355
        self.y = y

        self.first = True

        self.thickness = 50
        self.heigt = 50
        self.vel = 15

        self.monica_to_right = pg.image.load('Game\Assets\monica_to_right.png')
        self.monica_to_right = pg.transform.scale(self.monica_to_right,(110,97))

        self.monica_to_left = pg.image.load('Game\Assets\monica_to_left.png')
        self.monica_to_left = pg.transform.scale(self.monica_to_left,(110,97))

        self.default_monica = self.monica_to_right

        self.player_left = True
        self.player_right = True

    def control(self):
        keys = pg.key.get_pressed()
        if self.y <= 45:
            self.y = 45
        if self.y >= 500:
            self.y = 500
        if keys[pg.K_w]:
            self.y -= self.vel
        if keys[pg.K_s]:
            self.y += self.vel

    def draw(self):

        keys = pg.key.get_pressed()

        if keys[pg.K_a]: 
            self.default_monica = self.monica_to_left
            self.x = 320
            self.player_right = False
            self.player_left = True

        elif keys[pg.K_d] :
            self.default_monica = self.monica_to_right
            self.x = 355
            self.player_left = False
            self.player_right = True

        self.win.blit(self.default_monica,(self.x,self.y))


class Bullet():
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

        self.sansao_to_right = pg.image.load('Game\Assets\sansao_to_right.png')
        self.sansao_to_right = pg.transform.scale(self.sansao_to_right,(50,50))
        self.sansao_to_left = pg.image.load('Game\Assets\sansao_to_left.png')
        self.sansao_to_left = pg.transform.scale(self.sansao_to_left,(50,50))

    def draw_right(self):
        self.win.blit(self.sansao_to_right, (self.x+50, self.y+30))
        self.x += 10

    def draw_left(self):
        self.win.blit(self.sansao_to_left, (self.x-10, self.y+20))
        self.x -= 10
