#!/usr/bin/python
# Herda os atributos da entidade
import pygame.key

from code.const import ENTITY_SPEED, WIN_HEIGHT, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT, PLAYER_KEY_DOWN, PLAYER_KEY_UP
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position) #herda da classe pai

    #Movimento de acordo com as teclas (setas) pressionadas
    def move(self, ):
        pressed_key = pygame.key.get_pressed() #tecla pressionada, enquanto ela estiver pressionada algo precisa acontecer
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0: #Se tecla para cima
            self.rect.centery -= ENTITY_SPEED[self.name] # Altera a posição do player no eixo y de acordo com a velocidade definida

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:  # Se tecla para baixo
            self.rect.centery += ENTITY_SPEED[self.name]  #Altera para baixo a posição do player

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # Se tecla para esquerda
            self.rect.centerx -= ENTITY_SPEED[self.name]  #Altera para o lado esquerdo

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_HEIGHT:  # Se tecla para direita
            self.rect.centerx += ENTITY_SPEED[self.name]  #Altera para baixo a posição do player
        pass
