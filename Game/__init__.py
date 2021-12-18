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

        screen_dimesion = (settings.WIDTH, settings.HEIGHT)

        self.screen = pg.display.set_mode(screen_dimesion)
        self.running = False

        self.player = monica.Hero(self.screen, y=275)
        self.scenery = background.Background(self.screen)

        pg.display.set_caption(settings.TITLE)

    def quit(self): 
        '''Game quit method.'''

        print('shuting down...')
        pg.quit()
        exit()

    def events(self, player, obstacles, bullet, shoots, shootsR): 
        '''Game events method.'''

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            
            # cebolinha
            if event.type == cebolinha.obstacle_timer:  # AND THE GAME IS ACTIVE
                obstacles.append(cebolinha.cebolinha.get_rect(
                    midbottom=(
                        random.choice([-(0.5*cebolinha.largura), cebolinha.WIDTH+(0.5*cebolinha.largura)]), random.randint(cebolinha.altura, cebolinha.HEIGHT)))
                    )

            # shoot
            if event.type == pg.KEYDOWN and event.key == pg.K_a and player.player_left:
                shoots.append(bullet)
            if event.type == pg.KEYDOWN and event.key == pg.K_d and player.player_right:
                shootsR.append(bullet)

            player.control()

    def draw(self, player, scene, shoots, shootsR): 
        '''Game draw method.'''

        # Game Loop Background reset
        scene.draw()

        # Draw Monica
        player.draw()

        # Draw bullets
        for shoot in shoots:
            shoot.draw_left()

        for shoot in shootsR:
            shoot.draw_right()

    def run(self):
        '''Game loop method.'''

        self.running = True
        clock = pg.time.Clock()

        shoots = []
        shootsR = []

        obstacle_timer = pg.USEREVENT + 1
        pg.time.set_timer(obstacle_timer, 1400)

        enemies = cebolinha.obstacle_rect_list

        # Game loop
        while self.running:

            projectile = monica.Bullet(self.screen, self.player.x, self.player.y)

            self.events(self.player, enemies, projectile, shoots, shootsR)
            self.draw(self.player, self.scenery, shoots, shootsR)

            enemies = cebolinha.obstacle_movement(enemies, shoots, shootsR)

            pg.display.update()

            clock.tick(settings.FPS)
