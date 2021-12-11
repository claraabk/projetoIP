import pygame
from sys import exit

FPS = 30
WIDTH = 800
HEIGHT = 600
BGCOLOR = (255, 255, 255)
GRIDCOLOR = "red"

TILESIZE = 50
GRIDWIDTH = WIDTH // TILESIZE
GRIDHEIGHT = HEIGHT // TILESIZE

# width of the street: 120px


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
grass = pygame.transform.scale(grass, (800, 600))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # background:
    screen.blit(grass, (0, 0))
    screen.blit(highway, highway_rect)

    # "default":
    pygame.display.update()
    clock.tick(FPS)
