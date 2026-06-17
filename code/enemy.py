# Enemy: move para a esquerda, atira automaticamente com delay configurável. Ambos herdam de Entity.

import pygame

from code.EnemyShot import EnemyShot
from code.const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)  # herda da classe pai
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    #Decrementa centerx a cada frame. EntityMediador zera a vida quando sai da tela
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  #sempre para a esquerda

    #Conta frames e quando o delay zera, cria um EnemyShot na posição atual do inimigo
    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))  #cria tiro do inimigo