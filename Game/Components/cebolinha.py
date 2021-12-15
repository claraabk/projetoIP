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
timer = 1000
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, timer)

# OBSTACLE LIST:
obstacle_rect_list = []

# CEBOLINHA SURFACE:
altura, largura = 40, 40

cebolinha_from_right = pygame.image.load('Game\Components\media\cebolinha_from_right.png')
cebolinha_from_right = pygame.transform.scale(cebolinha_from_right,(82,90))
cebolinha_from_left = pygame.image.load('Game\Components\media\cebolinha_from_left.png')
cebolinha_from_left = pygame.transform.scale(cebolinha_from_left,(90,90))

cebolinha = cebolinha_from_right

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
    global timer
    if lista:
        for obstaculo in lista:
            if obstaculo.left == esquerda or obstaculo.right == direita:
                lista.remove(obstaculo)
                vida_monica -= 1
                print("VIDA:", vida_monica)
                
            if esquerda < obstaculo.left <= WIDTH:
                obstaculo.x -= 1
                cebolinha = cebolinha_from_right
            elif obstaculo.right < direita:
                obstaculo.x += 1
                cebolinha = cebolinha_from_left

            for shoot in shoots:
                if (shoot.x > obstaculo.x and shoot.x < obstaculo.x + 40 and 
                    shoot.y > obstaculo.y - 60 and shoot.y < obstaculo.y + 40):
                    dead_cebolinhas += 1
                    timer -= 100
                    print("CEBOLINHAS:", dead_cebolinhas)
                    lista.remove(obstaculo)
                    shoots.remove(shoot)
            
            for shoot in shootsR:
                if (shoot.x > obstaculo.x and shoot.x < obstaculo.x + 40 and 
                    shoot.y > obstaculo.y - 60 and shoot.y < obstaculo.y + 40):
                    dead_cebolinhas += 1
                    print("CEBOLINHAS:", dead_cebolinhas)
                    shootsR.remove(shoot)
                    lista.remove(obstaculo)

            screen.blit(cebolinha, obstaculo)
        return lista
    else:
        return []
