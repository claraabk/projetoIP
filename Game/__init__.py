'''
Initialize all game files.
'''

# Native
from sys import exit

# Site-packages
import pygame as pg

# Locals
from Game import settings
from Game.Components import monica
from Game.Components import background

class GameLoop:
    '''
    Define Game Loop class.
    '''

    def __init__(self):
        '''Initialize game window.'''
        
        pg.init()

        screenDim = (settings.WIDTH, settings.HEIGHT)

        self.screen = pg.display.set_mode(screenDim)
        self.running = False

        pg.display.set_caption(settings.TITLE)
    
    def update(self):
        '''Game update rule and components method.'''
        pass

    def draw_grid(self):
        '''Develop game draw grid method.'''

        x, y = (0, 0)

        for _ in range(settings.WIDTH):
            x += settings.GRIDWIDTH
            pg.draw.line(self.screen, settings.GRIDCOLOR, (x, 0), (x, settings.HEIGHT))

        for _ in range(settings.HEIGHT):
            y += settings.GRIDHEIGHT
            pg.draw.line(self.screen, settings.GRIDCOLOR, (0, y), (settings.WIDTH, y))

        
    def draw(self, player, bullet, grid_on=False): 
        '''Game draw method.'''

        # Game Loop Background reset
        self.screen.blit(background.grass, (0,0))
        self.screen.blit(background.highway, background.highway_rect)

        # Draw a grid on game (DEBUG FUNCTION)
        if grid_on:
            self.draw_grid()

        # Draw Monica
        player.draw()

        # Draw Shooting

        # Update display
        # pg.display.flip() - I dont know what flip() do
        pg.display.update()

    def quit(self): 
        '''Game quit method.'''

        print('shuting down...')
        pg.quit()
        exit()
    
    def events(self, player, bullet): 
        '''Game events method.'''

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            player.control()

    def run(self):
        '''Game loop method.'''

        self.running = True
        clock = pg.time.Clock()
        player = monica.Hero(self.screen, 375, 275)
        bullet_group = pg.sprite.Group()


        # Game loop
        while self.running:
            clock.tick(settings.FPS)

            self.events(player, bullet_group)
            self.update()
            self.draw(player, bullet_group, grid_on=False)
