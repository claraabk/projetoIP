from random import randint
import pygame as pg


class Buff():
    def __init__(self, screen):
        self.screen = screen
        self.x = 355
        self.y = randint(92, 540)
        self.effect = randint(0, 4)
        self.in_screen = False
        self.buff_image = pg.image.load('Game\Assets\imgbuff_heart.png')
        self.buff_rect = self.buff_image.get_rect()
    
    def draw(self):
        if self.effect == 0:
            buff_image = pg.image.load('Game\Assets\imgbuff_heart.png')
        elif self.effect == 2 or self.effect == 4:
            buff_image = pg.image.load('Game\Assets\imgbuff_ray.png')
        else:
            buff_image = pg.image.load('Game\Assets\imgdebuff.png')

        buff_image = pg.transform.scale(buff_image,(80,50))  # Please don't change this ;)

        self.buff_image = buff_image
        self.buff_rect = buff_image.get_rect()

        self.screen.blit(buff_image,(self.x,self.y))
