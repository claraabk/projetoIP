import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800, 600))
done = False

empty_street = True
 
 
class Buff():
    '''create buff class'''
 
    def __init__(self):
 
        self.x = 400
        self.y = random.randint(0,600)
        efeito = random.randint(0,2)

    def draw(self, efeito):
 
        if efeito == 0:
            pg.draw.circle(screen, (255,0,0), (self.x, self.y), 30)
        elif efeito == 1:
            pg.draw.circle(screen, (0,255,0), (self.x, self.y), 30)
        elif efeito == 2:
            pg.draw.circle(screen, (0,0,255), (self.x, self.y), 30)

while not done:
    chance = random.randint(0,6)
    
    screen.fill((0, 0, 0))

    if chance > 3:
        test_buff = Buff()
        
        test_buff.draw(random.randint(0, 2))
        pg.time.delay(3000)

    
    for event in pg.event.get():
                if event.type == pg.QUIT:
                        done = True
    
        
    pg.display.update()