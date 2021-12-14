import pygame as pg

#default
pg.init()
screen = pg.display.set_mode((800,600)) 

#abstract class for all scoring components
class Score:
  
    def __init__(self):
        self.score = 0
        self.score_font = pg.font.Font("monicafont.ttf", 150)
        pg.display
    
    def update(self):
      ''' empty method for updating scores '''
        pass

#implementing buffs acquired
class Buffs(Score):
  
    def update(self):
        if got_buff:
            self.score += 1

#implementing points for each hit monica makes
class Hits(Score):
  
    def update(self):
        if monica_hit: 
            self.score += 1

#implementing life loss for each cebolinha that gets to the street
class Life:
  
    def __init__(self):
        self.count = 3
        self.count_font = pg.font.Font("monicafont.ttf", 150)

    def update(self):
        if cebolinha_street:
            self.count -= 1

        if life_bonus and self.count < 3:
            self.count += 1

