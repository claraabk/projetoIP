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

# CONSTANTES
RANGE_TIMER = random.randint(2, 4)
VELOCIDADE_CEBOLINHA = 5

# limites do background:
TAMANHO_RUA = 120
direita = (WIDTH-TAMANHO_RUA)/2
esquerda = WIDTH - ((WIDTH-TAMANHO_RUA)/2)

# "default":
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Background")
clock = pygame.time.Clock()


# TIMER:
# buff_timer = pygame.USEREVENT + 1
cebolinha_timer = pygame.event.custom_type()
pygame.time.set_timer(cebolinha_timer, RANGE_TIMER*1000)

buff_timer = pygame.event.custom_type()
pygame.time.set_timer(buff_timer, 2000)

buff_list = []
buff_screen = pygame.Surface((40, 40))
buff_screen.fill("#9ec4e8")
buff_2_screen = pygame.Surface((40, 40))
buff_2_screen.fill("Red")

# OBSTACLE LIST:
obstacle_rect_list = []

# sufaces
background = pygame.Surface((800, 600))
background.fill("#d79ee8")


# CEBOLINHA SURFACE:
altura, largura = 40, 40
cebolinha = pygame.Surface((altura, largura))
cebolinha.fill("#f2e18d")


times = 0
bufff = False
bufff2 = False

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
                    obstaculo.x -= VELOCIDADE_CEBOLINHA
                elif obstaculo.right < direita:
                    obstaculo.x += VELOCIDADE_CEBOLINHA

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
        if event.type == cebolinha_timer:  # AND THE GAME IS ACTIVE
            obstacle_rect_list.append(cebolinha.get_rect(
                midbottom=(random.choice([-(0.5*largura), WIDTH+(0.5*largura)]), random.randint(altura, HEIGHT))))
        if event.type == buff_timer:  # AND THE GAME IS ACTIVE
            buff_rect = buff_screen.get_rect(
                midbottom=(WIDTH/2, random.randint(altura, HEIGHT)))
            buff_2_rect = buff_2_screen.get_rect(
                midbottom=(WIDTH/2, random.randint(altura, HEIGHT)))
            if times != 0 and times % 3 == 0:
                bufff2 = True
            else:
                bufff2 = False
            if times % 2 == 0:
                bufff = True
            else:
                bufff = False
            times += 1

    screen.blit(background, (0, 0))
    if bufff == True:
        screen.blit(buff_screen, buff_rect)
    if bufff2 == True:
        screen.blit(buff_2_screen, buff_2_rect)

    # RUNNING THE SPAWN
    # aqui ele vai robar o blit dos cebolinhas, ent vai ter movimento
    # e vai updatar a obstacle_rect_list
    obstacle_rect_list = obstacle_movement(obstacle_rect_list)
    # for i in buff_list:
    #     screen.blit(buff_screen, i)

    # "default":
    pygame.display.update()
    clock.tick(FPS)
