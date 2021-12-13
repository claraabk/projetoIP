import pygame
from sys import exit
# CEBOLINHA:
from Game import settings 

class Enemies():

    # limites do background:
    TAMANHO_RUA = 120
    direita = (settings.WIDTH-TAMANHO_RUA)/2
    esquerda = settings.WIDTH - ((settings.WIDTH-TAMANHO_RUA)/2)

    def __init__(self, screen):
        self.screen = screen
        self.altura = 40
        self.largura = 40
    
    def draw(self):
        self.cebolinha = pygame.Surface((self.altura, self.largura))
        self.cebolinha.fill("#f2e18d")

    def move(self, lista):
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

                self.screen.blit(self.draw(), obstaculo)
            return lista
        else:
            return []
