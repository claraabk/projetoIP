'''
December 2021
Add Background class to the game.
IP Project  - Dono da Lua

@authors: Roseane Oliverira, Clara Kenderessy, Matheus Silva
'''


import pygame


class Background():

    pygame.display.set_caption("Background")

    scenary = pygame.image.load('Game\Assets\definitiveback.jpg')
    scenary = pygame.transform.scale(scenary, (800, 600))

    def __init__(self, screen):
        self.screen = screen
    
    def draw(self):
        self.screen.blit(self.scenary, (0, 0))
