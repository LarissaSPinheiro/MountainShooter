#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.entity import Entity
from code.entityFactory import EntityFactory

from code.const import COLOR_WHITE, WIN_WEIGHT


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode #modo do jogo 1 jogador, 2 etc
        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) #pega os objetos do nivel 1 e joga na lista
        self.timeout = 20000 # 20 segundos

    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3') #Adicionada musica ao Level 1
        pygame.mixer_music.play(-1) #Executar indefinidamente
        clock = pygame.time.Clock() #Executa conforme um tempo específico
        while True:
            clock.tick(60)  #Tempo de "passagem" da tela
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect) #desenha a imagem em tela
                ent.move()
            #Evento para fechar a janela no nível 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10 ,5))  # Mostra o tempo de duração da fase
            self.level_text(14, f'fps: {clock.get_fps() :.0f}s', COLOR_WHITE, (10, WIN_WEIGHT - 35))  # Print do clock em tela, imprime o FPS do game
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_WEIGHT - 20))  # Depuração do código, demonstra quantas entidades há em tela
            pygame.display.flip() #mostra em tela
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0],top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)


