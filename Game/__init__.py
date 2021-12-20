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

        self.missed_bullet_r = 2
        self.missed_bullet_l = 2

        self.shootsL = []
        self.shootsR = []

        self.challenge = spawn.SpawnCebolinha(self.screen)
        self.enemies = self.challenge.obstacle_rect_list

        self.monica_life = self.challenge.life_monica
        self.score = self.challenge.dead_cebolinhas

        self.gameover = False
        self.gameon = False

        self.flag = True
        self.sound_gameover = None

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

        if self.player.vel > 18:
            self.player.vel = 18
            print(f'[LIMIT] VEL: {self.player.vel}')
                
        if self.player.vel < 6:
            self.player.vel = 6
            print(f'[LIMIT] VEL: {self.player.vel}')

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

        if not self.gameon :  # In the menu
            menu = pg.image.load('Game\Assets\menu_background.jpeg')
            menu = pg.transform.scale(menu,(800,600))

            self.enemies = False

            self.screen.blit(menu,(0,0))

            keys = pg.key.get_pressed()

            if keys[pg.K_RETURN]:
                self.gameon = True
        else :

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
            
            # Penality Abusive Samuel Marsaro Mechanics
                if len(shoots_left) > self.missed_bullet_l:
                    player.vel -= 1
                    self.missed_bullet_l += 2
                    print(f'[PENALITY_LEFT] VEL DOWN: {player.vel}')
                
                if len(shoots_right) > self.missed_bullet_r:
                    player.vel -= 1
                    self.missed_bullet_r += 2
                    print(f'[PENALITY_RIGHT] VEL DOWN: {player.vel}')
            
            # Draw Monica Hearts Effect
            if self.challenge.life_monica > 3:
                self.challenge.life_monica = 3

            if self.challenge.life_monica == 3 :
                self.screen.blit(self.challenge.three_hearts,(650, -12))
            elif self.challenge.life_monica == 2 :
                self.screen.blit(self.challenge.two_hearts,(650, -12))
            elif self.challenge.life_monica == 1 :
                self.screen.blit(self.challenge.one_heart,(650, -12))
            elif self.challenge.life_monica == 0 :

                # stop background loop music 
                pg.mixer.music.stop()
                
                # launches the cebolinha win sounds
                if self.flag:
                    sound_gameover = pg.mixer.Sound('Game\Sounds\soundgameover.wav')
                    sound_gameover.set_volume(0.05)
                    sound_gameover.play()
                    self.flag = False
                    self.sound_gameover = sound_gameover

                # signals the game over
                self.gameover = True

                # temporarily shuts off cebolinhas spawn
                self.enemies = False
                
                # load gameover screen
                background = pg.image.load('Game\Assets\gameover_screen.jpg')
                background = pg.transform.scale(background,(800,600))

                self.screen.blit(background,(0,0))

                # wait space press to continue or esq to quit
                keys = pg.key.get_pressed()

                if keys[pg.K_SPACE]:  # Reset atributes of GameLoop class
                    self.sound_gameover.stop()
                    self.gameover = False
                    self.enemies = self.challenge.obstacle_rect_list
                    self.challenge.dead_cebolinhas = 0 
                    self.count_buff = 0
                    self.challenge.life_monica = 3
                    self.missed_bullet_l = 3
                    self.missed_bullet_r = 3
                    self.shootsL = []
                    self.shootsR = []
                    self.player.vel = 15
                    self.flag = True
                    self.sound_gameover = None
                    self.scenery.draw()

                    pg.mixer.music.load('Game\Sounds\Dancing_on_the_Street_NES.wav')
                    pg.mixer.music.set_volume(0.05)
                    pg.mixer.music.play(-1)

                    print('\nRESET GAME...')
                    print(f'VEL: {self.player.vel}')
                    print(f'LIFES: {self.challenge.life_monica}')
                    print(f'SCORE: {self.challenge.dead_cebolinhas}')
                    print(f'ENEMIES: activate')
                    print(f'SCENARY: activate\n')
            
            if not self.gameover:

                # Draw score
                pg.font.init()
                myfont = pg.font.SysFont('Comic Sans MS', 28)

                textscore = myfont.render(str(self.challenge.dead_cebolinhas), False, (0, 0, 0))
                self.screen.blit(textscore,(600,4))

                textbuff = myfont.render(str(self.count_buff), False, (0, 0, 0))
                self.screen.blit(textbuff,(460,4))

                if self.challenge.dead_cebolinhas > 20:

                    # Draw buff
                    self.buff.draw()

                    # get a "virtual" rect of player and buff
                    player_rect = pg.Rect(player.x, player.y, 40, 80)
                    buff_rect = pg.Rect(self.buff.x, self.buff.y, 40, 20)

                    if buff_rect.colliderect(player_rect):  # Collision effects
                    
                        if self.buff.effect == 0:  # Life bufff
                            self.challenge.life_monica += 1
                            player.vel = 15

                            sound_effect = pg.mixer.Sound('Game\Sounds\Menu1A.wav')
                            sound_effect.set_volume(0.05)
                            sound_effect.play()

                            print(f'[LIFE_BUFF] VEL RESET: {player.vel}')

                        # Ray buff
                        elif  self.buff.effect == 2 or self.buff.effect == 4:
                            self.count_buff += 1
                            player.vel += 1

                            sound_effect = pg.mixer.Sound('Game\Sounds\Item1A.wav')
                            sound_effect.set_volume(0.05)
                            sound_effect.play()

                            print(f'[RAY_BUFF] VEL UP: {player.vel}')
                        
                        # Ray debuff
                        else:
                            if player.vel >= 15:
                                player.vel -= 2
                            else:
                                player.vel -= 0.5

                            sound_effect = pg.mixer.Sound('Game\Sounds\Item1B.wav')
                            sound_effect.set_volume(0.05)
                            sound_effect.play()

                            print(f'[RAY_DEBUFF] VEL DOWN: {player.vel}')
                    
                        # make the buff disappear
                        self.buff.x = 1000
                        self.buff.y = 1000  

    def run(self):
        '''Game loop method.'''
        self.running = True

        clock = pg.time.Clock()

        obstacle_timer = pg.event.custom_type()
        pg.time.set_timer(obstacle_timer, 1180)

        buff_timer = pg.event.custom_type()
        pg.time.set_timer(buff_timer, 5000)

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
