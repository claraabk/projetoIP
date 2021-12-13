import pygame

from Game import settings 
#from sys import exit

# width of the street: 120px

class Background():

    pygame.display.set_caption("Background")

    highway = pygame.image.load("Game\Components\media\highway.png")
    highway = pygame.transform.scale(highway, (120, 600))
    highway_rect = highway.get_rect(center=(400, 300))

    grass = pygame.image.load("Game\Components\media\grass.png")
    grass = pygame.transform.scale(grass, (800, 600))

    def __init__(self, screen):
        self.screen = screen
    
    def draw(self):
        self.screen.blit(self.grass, (0, 0))
        self.screen.blit(self.highway, self.highway_rect)
