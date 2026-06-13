#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.EnemyShot import EnemyShot
from code.const import WIN_WIDTH, ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)  # herda da classe pai
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.score = 0

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]  #chegue no final e ponto

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))  # instancia os tiros do jogador 1 e 2 no meio do jogador, e fazer mover para direita