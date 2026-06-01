#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode #modo do jogo 1 jogador, 2 etc
        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) #pega os objetos do nivel 1 e joga na lista

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect) #desenha a imagem em tela
                ent.move()
            pygame.display.flip() #mostra em tela
        pass

