import pygame

FPS = 30
WIDTH = 800
HEIGHT = 600

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

dead_cebolinhas = 0
vida_monica = 3

# FUNÇÃO QUE MOVIMENTA OS CEBOLINHAS:
def obstacle_movement(lista, shoots, shootsR):
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
    global dead_cebolinhas 
    global vida_monica
    if lista:
        for obstaculo in lista:
            if obstaculo.left == esquerda or obstaculo.right == direita:
                lista.remove(obstaculo)
                vida_monica -= 1
                
            if esquerda < obstaculo.left <= WIDTH:
                obstaculo.x -= 1
            elif obstaculo.right < direita:
                obstaculo.x += 1

            for shoot in shoots:
                if (shoot.x > obstaculo.x and shoot.x < obstaculo.x + 40 and 
                    shoot.y > obstaculo.y - 20 and shoot.y < obstaculo.y + 20):
                    dead_cebolinhas += 1
                    lista.remove(obstaculo)
                    shoots.remove(shoot)
            
            for shoot in shootsR:
                if (shoot.x > obstaculo.x and shoot.x < obstaculo.x + 40 and 
                    shoot.y > obstaculo.y - 20 and shoot.y < obstaculo.y + 20):
                    dead_cebolinhas += 1
                    shootsR.remove(shoot)
                    lista.remove(obstaculo)

            screen.blit(cebolinha, obstaculo)
        return lista
    else:
        return []
