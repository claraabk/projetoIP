'''
December 2021
Initialize all game files.
IP Project  - Dono da Lua

@authors: 
   Beatriz Férre, Clara Kenderessy, Matheus Silva, 
   Roseane Oliveira, Rafael Baltar, Samuel Marsaro.
'''


# Native
from sys import exit
from random import randint, choice

# Site-packages
import pygame as pg

# Locals
from Game import settings
from Game.Components import gamester
from Game.Components import background
from Game.Components import spawn
from Game.Components import powerup


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

        self.player = gamester.Hero(self.screen)
        self.scenery = background.Background(self.screen)
        self.buff = powerup.Buff(self.screen)

        self.count_buff = 0

        self.missed_bullet_r = 1
        self.missed_bullet_l = 1

        self.shootsL = []
        self.shootsR = []

        self.challenge = spawn.SpawnCebolinha(self.screen)
        self.enemies = self.challenge.obstacle_rect_list

        self.monica_life = self.challenge.life_monica
        self.score = self.challenge.dead_cebolinhas

        pg.mixer.music.load('Game\Sounds\Dancing_on_the_Street_NES.wav')
        pg.mixer.music.set_volume(0.05)
        pg.mixer.music.play(-1)

        pg.display.set_caption(settings.TITLE)

    def quit(self): 
        '''Game quit method.'''

        print('shuting down...')
        pg.quit()
        exit()
    
    def update(self):
        '''Game update limit rules.'''

        if self.player.vel > 20:
            self.player.vel = 20
            print(f'VEL LIMIT: {self.player.vel}')
                
        if self.player.vel < 3:
            self.player.vel = 3
            print(f'VEL LIMIT: {self.player.vel}')

    def events(self, player, obstacles, obstacle_timer, bullet, shoots_left, shoots_right, buff_timer): 
        '''Game events method.'''

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

            # Cebolinhas creation
            if event.type == obstacle_timer:
                obstacles.append(
                    self.challenge.cebolinha.get_rect(
                        midbottom=(
                            choice(
                                [-(0.5 * self.challenge.width), 
                                settings.WIDTH + (0.5 * self.challenge.width)]),
                            randint(
                                self.challenge.height, settings.HEIGHT
                            )))
                )

            # shoot
            if event.type == pg.KEYDOWN and event.key == pg.K_a and player.player_left:
                shoots_left.append(bullet)
                sound_effect = pg.mixer.Sound('Game\Sounds\sfx_throw.wav')
                sound_effect.set_volume(0.05)
                sound_effect.play()
            if event.type == pg.KEYDOWN and event.key == pg.K_d and player.player_right:
                shoots_right.append(bullet)
                sound_effect = pg.mixer.Sound('Game\Sounds\sfx_throw.wav')
                sound_effect.set_volume(0.05)
                sound_effect.play()
            
            # buff
            if event.type == buff_timer:
                if randint(0, 1): # Basically True or False with 50% | 50% to drop other buff
                    self.buff = powerup.Buff(self.screen)

            player.control() 

    def draw(self, player, scene, shoots_left, shoots_right): 
        '''Game draw method.'''

        # Game Loop Background reset
        scene.draw()

        # Draw Monica
        player.draw()

        # Draw bullets
        if len(shoots_left)>=1 or len(shoots_right)>=1:
            for shoot in shoots_left:
                shoot.draw_left()

            for shoot in shoots_right:
                shoot.draw_right()
        
        # Penality Abusive Samuel Mechanics
        if len(shoots_left)>= self.missed_bullet_l:
            player.vel -= 0.5
            self.missed_bullet_l += 1
            print(f'VEL DOWN: {player.vel}')
        
        if len(shoots_right)>= self.missed_bullet_r:
            player.vel -= 0.5
            self.missed_bullet_r += 1 
            print(f'VEL DOWN: {player.vel}')
             
        # Draw Monica Hearts Effect
        if self.challenge.life_monica > 3:
            self.challenge.life_monica = 3

        if self.challenge.life_monica == 3 :
            self.screen.blit(self.challenge.three_hearts,(650, -12))
        elif self.challenge.life_monica == 2 :
            self.screen.blit(self.challenge.two_hearts,(650, -12))
        elif self.challenge.life_monica == 1 :
            self.screen.blit(self.challenge.one_heart,(650, -12))
        
        # Draw score and collected buffs
        pg.font.init()
        myfont = pg.font.SysFont('Comic Sans MS', 28)

        textscore = myfont.render(str(self.challenge.dead_cebolinhas), False, (0, 0, 0))
        self.screen.blit(textscore,(600,4))

        textbuff = myfont.render(str(self.count_buff), False, (0, 0, 0))
        self.screen.blit(textbuff,(460,4))

        # Draw buff
        if self.challenge.dead_cebolinhas > 10:
            self.buff.draw()

            player_rect = pg.Rect(player.x, player.y, 40, 80)
            buff_rect = pg.Rect(self.buff.x, self.buff.y, 40, 20)

            # Collision effects
            if buff_rect.colliderect(player_rect):
                
                # Life bufff
                if self.buff.effect == 0:
                    self.challenge.life_monica += 1
                    player.vel = 15

                    sound_effect = pg.mixer.Sound('Game\Sounds\Menu1A.wav')
                    sound_effect.set_volume(0.05)
                    sound_effect.play()

                    print(f'VEL RESET: {player.vel}')
                
                # Ray buff
                elif  self.buff.effect == 2 or self.buff.effect == 4:
                    self.count_buff += 1
                    player.vel += 1

                    sound_effect = pg.mixer.Sound('Game\Sounds\Item1A.wav')
                    sound_effect.set_volume(0.05)
                    sound_effect.play()

                    print(f'VEL UP: {player.vel}')
                
                # Ray debuff
                else:
                    if player.vel >= 15:
                        player.vel -= 2
                    else:
                        player.vel -= 0.5

                    sound_effect = pg.mixer.Sound('Game\Sounds\Item1B.wav')
                    sound_effect.set_volume(0.05)
                    sound_effect.play()

                    print(f'VEL DOWN: {player.vel}')
                
                self.buff.x = 1000
                self.buff.y = 1000

    def run(self):
        '''Game loop method.'''

        self.running = True
        clock = pg.time.Clock()

        obstacle_timer = pg.event.custom_type()
        pg.time.set_timer(obstacle_timer, 1100)

        buff_timer = pg.event.custom_type()
        pg.time.set_timer(buff_timer, 5000)

        # Game loop
        while self.running:

            projectile = gamester.Bullet(self.screen, self.player.x, self.player.y)

            self.events(
                self.player, self.enemies, 
                obstacle_timer, projectile, 
                self.shootsL, self.shootsR,
                buff_timer
            )

            self.draw(
                self.player, self.scenery, 
                self.shootsL, self.shootsR
            )

            self.update()

            self.challenge.load_rules(self.enemies, self.shootsL, self.shootsR)
            self.enemies = self.challenge.obstacle_rect_list

            pg.display.flip()

            clock.tick(settings.FPS)
