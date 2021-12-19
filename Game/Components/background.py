'''
December 2021
Add Background class to the game.
IP Project  - Dono da Lua

@authors: Roseane Oliverira, Clara Kenderessy, Matheus Silva
'''


import pygame


class Background():

    pygame.display.set_caption("Background")

    highway = pygame.image.load('Game\Assets\highway.png')
    highway = pygame.transform.scale(highway, (120, 600))
    highway_rect = highway.get_rect(center=(400, 300))

    grass = pygame.image.load('Game\Assets\definitiveback.jpg')
    grass = pygame.transform.scale(grass, (800, 600))

    def __init__(self, screen):
        self.screen = screen
    
    def draw(self):
        self.screen.blit(self.grass, (0, 0))
