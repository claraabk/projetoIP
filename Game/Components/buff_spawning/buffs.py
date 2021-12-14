import pygame as pg
import random
 
# DEFAULT:
pg.init()
 
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
 
# TIMER:
duration_timer = pg.USEREVENT + 1
pg.time.set_timer(duration_timer, 3000)
 
class Buff():
    '''create buff class'''
 
    
    def __init__(self):
        '''randomize de Y position to make buff appear anywhere'''
 
        self.x = 400
        self.y = random.randint(0,600)
 
        '''randomize the effect the buff has on the player'''
        efeito = random.randint(0,2)
 
    def update(self,x,y):
        '''create a method to alter the x and y positions to make
        the buff disappear when it's collected'''
        self.x = x
        self.y = y 
    
    def draw(self, efeito):
        '''display buff with correspondent determined effect'''
 
        if efeito == 0:
            pg.draw.circle(screen, (255,0,0), (self.x, self.y), 30)
 
        elif efeito == 1:
            pg.draw.circle(screen, (0,255,0), (self.x, self.y), 30)
 
        elif efeito == 2:
            pg.draw.circle(screen, (0,0,255), (self.x, self.y), 30)
 
 
done = False
 
while not done:
    '''determine the chance for a buff to be instantiated'''
    chance = random.randint(0,10)
 
    screen.fill((0, 0, 0))
    test_buff = Buff()
 
 
    for event in pg.event.get():
        if event.type == duration_timer:
            if chance > 9: 
                test_buff.draw(random.randint(0, 2))
            
            pg.display.update()
        if event.type == pg.QUIT:
            done = True
