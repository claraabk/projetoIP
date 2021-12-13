import pygame
from sys import exit
# CEBOLINHA:
from Game import settings 

class Enemies():

    # limites do background:
    TAMANHO_RUA = 120
    direita = (settings.WIDTH-TAMANHO_RUA)/2
    esquerda = settings.WIDTH - ((settings.WIDTH-TAMANHO_RUA)/2)
    obstacle_rect_list = []

    def __init__(self, screen):
        self.screen = screen
        self.altura = 40
        self.largura = 40
        self.cebolinha = pygame.Surface((self.altura, self.largura))
    
    def draw(self):
        self.cebolinha = pygame.Surface((self.altura, self.largura))
        self.cebolinha.fill("#f2e18d")

    def spawn(self, lista):

        if lista:
            for obstaculo in lista:
                if obstaculo.left == self.esquerda or obstaculo.right == self.direita:
                    # dá pra colocar um contador de cebolinhas aqui
                    lista.remove(obstaculo)
                else:
                    if self.esquerda < obstaculo.left <= settings.WIDTH:
                        obstaculo.x -= 5
                    elif obstaculo.right < self.direita:
                        obstaculo.x += 5

                self.screen.blit(self.cebolinha.fill("#f2e18d"), obstaculo)
            return lista
        else:
            return []

'''
import pygame
from sys import exit
# CEBOLINHA:
import random

FPS = 30
WIDTH = 800
HEIGHT = 600
BGCOLOR = (255, 255, 255)
GRIDCOLOR = "red"

TILESIZE = 50
GRIDWIDTH = WIDTH // TILESIZE
GRIDHEIGHT = HEIGHT // TILESIZE

# limites do background:
TAMANHO_RUA = 120
direita = (WIDTH-TAMANHO_RUA)/2
esquerda = WIDTH - ((WIDTH-TAMANHO_RUA)/2)

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
grass = pygame.transform.scale(grass, (WIDTH, HEIGHT))

# TIMER:
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)

# OBSTACLE LIST:
obstacle_rect_list = []

# CEBOLINHA SURFACE:
altura, largura = 40, 40
cebolinha = pygame.Surface((altura, largura))
cebolinha.fill("#f2e18d")


# FUNÇÃO QUE MOVIMENTA OS CEBOLINHAS:
def obstacle_movement(lista):
    """ 
    A função movimenta os cebolinhas e os elimina quando chegam à rua.
    :param list: lista com os retângulos dos cebolinhas.
    :returns: a lista com os cebolinhas updatados.
    """
    # ?eu nn sei se precisa de tanto global :/?
    global largura
    global cebolinha
    global direita
    global esquerda
    if lista:
        for obstaculo in lista:
            if obstaculo.left == esquerda or obstaculo.right == direita:
                # dá pra colocar um contador de cebolinhas aqui
                lista.remove(obstaculo)
            else:
                if esquerda < obstaculo.left <= WIDTH:
                    obstaculo.x -= 5
                elif obstaculo.right < direita:
                    obstaculo.x += 5

            screen.blit(cebolinha, obstaculo)
        return lista
    else:
        return []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # CRIANDO CEBOLINHAS TD VEZ Q O TIMER ACIONA
        if event.type == obstacle_timer:  # AND THE GAME IS ACTIVE
            obstacle_rect_list.append(cebolinha.get_rect(
                midbottom=(random.choice([-(0.5*largura), WIDTH+(0.5*largura)]), random.randint(altura, HEIGHT))))

    # background:
    screen.blit(grass, (0, 0))
    screen.blit(highway, highway_rect)

    # RUNNING THE SPAWN
    # aqui ele vai robar o blit dos cebolinhas, ent vai ter movimento
    # e vai updatar a obstacle_rect_list
    obstacle_rect_list = obstacle_movement(obstacle_rect_list)

    # "default":
    pygame.display.update()
    clock.tick(FPS)
'''
