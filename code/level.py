#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.EntityMediator import EntityMediator
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory

from code.const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN
from code.player import Player

from code.entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.timeout = 20000  # 20 segundos
        self.name = name
        self.game_mode = game_mode #modo do jogo 1 jogador, 2 etc
        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) #pega os objetos do nivel 1 e joga na lista
        self.entity_list.append(EntityFactory.get_entity('Player1')) #Inicializa pelo construtor a nave 1
        if game_mode in [MENU_OPTION[1], MENU_OPTION [2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))  # Inicializa pelo construtor a nave 2
        # a CADA X tempo teremos um inimigo
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)


    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3') #Adicionada musica ao Level 1
        pygame.mixer_music.play(-1) #Executar indefinidamente
        clock = pygame.time.Clock() #Executa conforme um tempo específico
        while True:
            clock.tick(60)  #Tempo de "passagem" da tela
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect) #desenha a imagem em tela
                ent.move() #move os player e enemys
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot) #colocar o meu tiro dentro das entidades
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health:{ent.health} | Score: {ent.score}', C_GREEN, (10 , 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health:{ent.health} | Score: {ent.score}', C_CYAN, (10 , 45))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            #printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10 , 5))  # Mostra o tempo de duração da fase
            self.level_text(14, f'fps: {clock.get_fps() :.0f}s', C_WHITE, (10, WIN_HEIGHT - 35))  # Print do clock em tela, imprime o FPS do game
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))  # Depuração do código, demonstra quantas entidades há em tela
            pygame.display.flip() #mostra em tela

            #Colisão
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0],top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)