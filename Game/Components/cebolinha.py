import pygame

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
                lista.remove(obstaculo)
                
            if esquerda < obstaculo.left <= WIDTH:
                obstaculo.x -= 1
            elif obstaculo.right < direita:
                obstaculo.x += 1

            screen.blit(cebolinha, obstaculo)
        return lista
    else:
        return []
