'''
Initialize all game files.
'''

# Native
from sys import exit
import random

# Site-packages
import pygame as pg

# Locals
from Game import settings
from Game.Components import monica
from Game.Components import background
from Game.Components import cebolinha

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

        
    def draw(self, player, enemies, scene, grid_on=False): 
        '''Game draw method.'''

        # Game Loop Background reset
        scene.draw()

        # Draw a grid on game (DEBUG FUNCTION)
        if grid_on:
            self.draw_grid()

        # Draw Cebolinhas
        enemies.draw()

        # Draw Monica
        player.draw()

        # Update display
        pg.display.update()

    def quit(self): 
        '''Game quit method.'''

        print('shuting down...')
        pg.quit()
        exit()
    
    def events(self, player, enemies): 
        '''Game events method.'''

        obstacle_timer = pg.USEREVENT + 1
        pg.time.set_timer(obstacle_timer, 1000)

        # OBSTACLE LIST:
        obstacle_rect_list = enemies.move([])

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            
            # cebolinha
            if event.type == obstacle_timer:
                obstacle_rect_list.append(enemies.cebolinha.get_rect(
                    midbottom=(random.choice(
                        [-(0.5 * enemies.largura), settings.WIDTH + (0.5 * enemies.largura)]
                    ), random.randint(enemies.altura, settings.HEIGHT))
                ))

            player.control()

    def run(self):
        '''Game loop method.'''

        self.running = True
        clock = pg.time.Clock()
        player = monica.Hero(self.screen, 375, 275)
        enemies = cebolinha.Enemies(self.screen)
        scenery = background.Background(self.screen)

        # Game loop
        while self.running:
            clock.tick(settings.FPS)

            self.events(player, enemies)
            self.update()
            self.draw(player, enemies, scenery, grid_on=False)
