import pygame as pg
from Game import settings


class Challenge():

    def __init__(self, screen):
        self.screen = screen
        self.obstacle_rect_list = []

        self.cebolinha_from_right = pg.image.load('Game\Assets\cebolinha_from_right.png')
        self.cebolinha_from_right = pg.transform.scale(self.cebolinha_from_right,(82,90))
        self.cebolinha_from_left = pg.image.load('Game\Assets\cebolinha_from_left.png')
        self.cebolinha_from_left = pg.transform.scale(self.cebolinha_from_left,(90,90))

        self.three_hearts = pg.image.load('Game\Assets\hree_hearts.png')
        self.three_hearts = pg.transform.scale(self.three_hearts,(200,70))
        self.two_hearts = pg.image.load('Game\Assets\wo_hearts.png')
        self.two_hearts = pg.transform.scale(self.two_hearts,(200,70))
        self.one_heart = pg.image.load('Game\Assets\one_heart.png')
        self.one_heart = pg.transform.scale(self.one_heart,(200,70))

        self.right = (settings.WIDTH - settings.STREET_SIZE) / 2
        self.left = settings.WIDTH - ((settings.WIDTH - settings.STREET_SIZE) / 2)

        self.height = 40 + 92
        self.width = 40

        self.vel = 1

        self.cebolinha = self.cebolinha_from_right

        self.dead_cebolinhas = 0
        self.life_monica = 3

    def load_rules(self, obstacles, shoots_left, shoots_right):

        if obstacles:
            for obstacle in obstacles:
                if obstacle.left == self.left or obstacle.right == self.right:
                    obstacles.remove(obstacle)
                    self.life_monica -= 1
                    print("VIDA:", self.life_monica)
                    sound_effect = pg.mixer.Sound('Game\Sounds\Menu1B.wav')
                    sound_effect.play()
            
                if self.left < obstacle.left <= settings.WIDTH:
                    obstacle.x -= 1
                    self.cebolinha = self.cebolinha_from_right
                elif obstacle.right < self.right:
                    obstacle.x += 1
                    self.cebolinha = self.cebolinha_from_left
                
                if len(obstacles) >= 1:
                    for shoot in shoots_left:
                        if (shoot.x > obstacle.x and shoot.x < obstacle.x + 40 and 
                            shoot.y > obstacle.y - 60 and shoot.y < obstacle.y + 40):
                            self.dead_cebolinhas += 1
                            print("CEBOLINHAS:", self.dead_cebolinhas)
                            obstacles.remove(obstacle)
                            shoots_left.remove(shoot)

                            sound_effect = pg.mixer.Sound('Game\Sounds\collision.flac')
                            sound_effect.play()
                    
                    for shoot in shoots_right:
                        if (shoot.x > obstacle.x and shoot.x < obstacle.x + 40 and 
                            shoot.y > obstacle.y - 60 and shoot.y < obstacle.y + 40):
                            self.dead_cebolinhas += 1
                            print("CEBOLINHAS:", self.dead_cebolinhas)
                            shoots_right.remove(shoot)
                            obstacles.remove(obstacle)

                            sound_effect = pg.mixer.Sound('Game\Sounds\collision.flac')
                            sound_effect.play()

                self.screen.blit(self.cebolinha, obstacle)
                pg.display.update(obstacle)

                self.obstacle_rect_list = obstacles
        else:
            self.obstacle_rect_list = []
