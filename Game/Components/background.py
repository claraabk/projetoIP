import pygame
from sys import exit
from Game import settings

# "default":
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Background")
clock = pygame.time.Clock()

# criando as surfaces:
highway = pygame.image.load("Game\Components\media\highway.png")
highway = pygame.transform.scale(highway, (120, 600))
highway_rect = highway.get_rect(center=(400, 300))
grass = pygame.image.load("Game\Components\media\grass.png")
grass = pygame.transform.scale(grass, (settings.WIDTH, settings.HEIGHT))
