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
from Game.Components.buff_spawning import buffs_Rr


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
            pg.draw.line(self.screen, settings.GRIDCOLOR,
                         (x, 0), (x, settings.HEIGHT))

        for _ in range(settings.HEIGHT):
            y += settings.GRIDHEIGHT
            pg.draw.line(self.screen, settings.GRIDCOLOR,
                         (0, y), (settings.WIDTH, y))

    def draw(self, player, scene, shoots, shootsR, grid_on=False):
        '''Game draw method.'''

        # Game Loop Background reset
        scene.draw()

        # Draw a grid on game (DEBUG FUNCTION)
        if grid_on:
            self.draw_grid()

        # Draw Monica
        player.draw()

        # Draw bullets
        for shoot in shoots:
            shoot.draw_left()

        for shoot in shootsR:
            shoot.draw_right()

    def quit(self):
        '''Game quit method.'''

        print('shuting down...')
        pg.quit()
        exit()

<<<<<<< Updated upstream
    def events(self, player, obstacles, shoots, shootsR):
=======
    def events(self, player, obstacles, shoots, shootsR, buff_timer):
>>>>>>> Stashed changes
        '''Game events method.'''

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            # cebolinha
            if event.type == cebolinha.obstacle_timer:  # AND THE GAME IS ACTIVE
                obstacles.append(cebolinha.cebolinha.get_rect(
                    midbottom=(
                        random.choice([-(0.5*cebolinha.largura), cebolinha.WIDTH+(0.5*cebolinha.largura)]), random.randint(cebolinha.altura+92, cebolinha.HEIGHT)))
                )
<<<<<<< Updated upstream
=======

            if event.type == buff_timer:  # AND THE GAME IS ACTIVE
                if buffs_Rr.times != 0 and buffs_Rr.times % 3 == 0:
                    buffs_Rr.bufff2 = True
                else:
                    buffs_Rr.bufff2 = False

                if buffs_Rr.times % 2 == 0:
                    buffs_Rr.bufff = True
                else:
                    buffs_Rr.bufff = False
                buffs_Rr.times += 1
>>>>>>> Stashed changes

            # shoot
            if event.type == pg.KEYDOWN and event.key == pg.K_a and player.player_left:
                shoots.append(monica.Bullet(self.screen, player.x, player.y))
            if event.type == pg.KEYDOWN and event.key == pg.K_d and player.player_right:
                shootsR.append(monica.Bullet(self.screen, player.x, player.y))

            player.control()

    def run(self):
        '''Game loop method.'''

        self.running = True
        clock = pg.time.Clock()

        player = monica.Hero(self.screen, 375, 275)
        scenery = background.Background(self.screen)

        shoots = []
        shootsR = []

        obstacle_timer = pg.event.custom_type()
        pg.time.set_timer(obstacle_timer, 1400)

        buff_timer = pg.event.custom_type()
        pg.time.set_timer(buff_timer, 5000)

        teste = cebolinha.obstacle_rect_list

        # Game loop
        while self.running:

            self.events(player, teste, shoots, shootsR, buff_timer)
            self.draw(player, scenery, shoots, shootsR, grid_on=False)

            teste = cebolinha.obstacle_movement(teste, shoots, shootsR)

            # tentando fazer a colisão (com um dos tipos de buff)
            # bug: ele faz a colisão com o buff antes mesmo dele aparecer na tela (deve ser por causa da lógica do retângulo)
            if buffs_Rr.buff_rect.collidepoint((player.x+55, player.y)) or buffs_Rr.buff_rect.collidepoint((player.x+55, player.y+97)):
                print("Colidiu!")
            # printando os buffs na tela
            if buffs_Rr.bufff == True:
                self.screen.blit(buffs_Rr.buff_screen, buffs_Rr.buff_rect)
            if buffs_Rr.bufff2 == True:
                self.screen.blit(buffs_Rr.buff_2_screen, buffs_Rr.buff_2_rect)
            self.update()
            pg.display.update()
            clock.tick(settings.FPS)
