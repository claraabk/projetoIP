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
from Game.Components import dynamics


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

        self.shootsL = []
        self.shootsR = []

        self.challenge = dynamics.Challenge(self.screen)
        self.enemies = self.challenge.obstacle_rect_list

        pg.display.set_caption(settings.TITLE)

    def quit(self): 
        '''Game quit method.'''

        print('shuting down...')
        pg.quit()
        exit()

    def events(self, player, obstacles, obstacle_timer, bullet, shoots_left, shoots_right): 
        '''Game events method.'''

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            # Challenge
            if event.type == obstacle_timer:
                obstacles.append(
                    self.challenge.cebolinha.get_rect(
                        midbottom=(
                            random.choice(
                                [-(0.5 * self.challenge.width), settings.WIDTH + (0.5 * self.challenge.width)]
                            ),
                            random.randint(
                                self.challenge.height, settings.HEIGHT
                            )
                        )
                    )
                )

            # shoot
            if event.type == pg.KEYDOWN and event.key == pg.K_a and player.player_left:
                shoots_left.append(bullet)
            if event.type == pg.KEYDOWN and event.key == pg.K_d and player.player_right:
                shoots_right.append(bullet)

            player.control()

    def draw(self, player, scene, shoots_left, shoots_right): 
        '''Game draw method.'''

        # Game Loop Background reset
        scene.draw()

        # Draw Monica
        player.draw()

        # Draw bullets
        for shoot in shoots_left:
            shoot.draw_left()

        for shoot in shoots_right:
            shoot.draw_right()
        
        # Draw Monica Hearts Effect
        if self.challenge.life_monica == 3 :
            self.screen.blit(self.challenge.three_hearts,(650,-12))
        elif self.challenge.life_monica == 2 :
            self.screen.blit(self.challenge.two_hearts,(650,-12))
        elif self.challenge.life_monica == 1 :
            self.screen.blit(self.challenge.one_heart,(650,-12))
        
        # Draw score
        pg.font.init()
        myfont = pg.font.SysFont('Comic Sans MS', 28)
        textsurface = myfont.render(str(self.challenge.dead_cebolinhas), False, (0, 0, 0))
        self.screen.blit(textsurface,(620,4))

    def run(self):
        '''Game loop method.'''

        self.running = True
        clock = pg.time.Clock()

        obstacle_timer = pg.event.custom_type()
        pg.time.set_timer(obstacle_timer, 1400)

        # Game loop
        while self.running:

            projectile = monica.Bullet(self.screen, self.player.x, self.player.y)

            self.events(
                self.player, self.enemies, 
                obstacle_timer, projectile, 
                self.shootsL, self.shootsR
            )

            self.draw(
                self.player, self.scenery, 
                self.shootsL, self.shootsR
            )

            self.challenge.load_rules(self.enemies, self.shootsL, self.shootsR)
            self.enemies = self.challenge.obstacle_rect_list

            pg.display.flip()

            clock.tick(settings.FPS)
