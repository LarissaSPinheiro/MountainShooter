#!/usr/bin/python
# Herda os atributos da entidade
import pygame.key

from code.PlayerShot import PlayerShot
from code.const import ENTITY_SPEED, WIN_HEIGHT, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT, PLAYER_KEY_DOWN, PLAYER_KEY_UP, \
    PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY, WIN_WIDTH
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position) #herda da classe pai
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    #Movimento de acordo com as teclas (setas) pressionadas
    def move(self, ):
        pressed_key = pygame.key.get_pressed() #tecla pressionada, enquanto ela estiver pressionada algo precisa acontecer
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0: #Se tecla para cima
            self.rect.centery -= ENTITY_SPEED[self.name] # Altera a posição do player no eixo y de acordo com a velocidade definida

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:  # Se tecla para baixo
            self.rect.centery += ENTITY_SPEED[self.name]  #Altera para baixo a posição do player

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # Se tecla para esquerda
            self.rect.centerx -= ENTITY_SPEED[self.name]  #Altera para o lado esquerdo

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:  # Se tecla para direita
            self.rect.centerx += ENTITY_SPEED[self.name]  #Altera para baixo a posição do player
        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed() #atirar
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery)) #instancia os tiros do jogador 1 e 2 no meio do jogador, e fazer mover para direita
