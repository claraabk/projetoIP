import pygame
from sys import exit
import random

FPS = 30
ALTURA, LARGURA = 40, 40
WIDTH = 800
HEIGHT = 600

# "default":
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Background")
clock = pygame.time.Clock()


# TIMER:
buff_timer = pygame.event.custom_type()
pygame.time.set_timer(buff_timer, 5000)

buff_screen = pygame.Surface((40, 40))
buff_screen.fill("#9ec4e8")
buff_2_screen = pygame.Surface((40, 40))
buff_2_screen.fill("Red")

# sufaces
background = pygame.Surface((800, 600))
background.fill("#d79ee8")


times = 0
bufff = False
bufff2 = False

buff_rect = buff_screen.get_rect(midbottom=(
    WIDTH/2-7, random.randint(ALTURA+92, HEIGHT)))
buff_2_rect = buff_2_screen.get_rect(midbottom=(
    WIDTH/2-7, random.randint(ALTURA+92, HEIGHT)))


if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == buff_timer:  # AND THE GAME IS ACTIVE
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

        # "default":
        pygame.display.update()
        clock.tick(FPS)
