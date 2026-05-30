#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH
from code.const import COLOR_ORANGE
from code.const import COLOR_WHITE
from code.const import MENU_OPTION

class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png') #carregando a imagem
        self.rect = self.surf.get_rect(left=0, top=0) #cria o retângulo
    def run(self, ):
        pygame.mixer_music.load('./asset/menu.mp3') #carrega a música
        pygame.mixer_music.play(-1) #toca a música (-1 continua tocando)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Adicionando a imagem ao retângulo
            self.menu_text(50, "Mountain", (COLOR_WHITE), ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", (COLOR_WHITE), ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], (COLOR_WHITE), ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            #Criasse o evento para finalizar a janela / #Check for all events
            for event in pygame.event.get(): #checa e pega os eventos
               if event.type == pygame.QUIT: #se o tipo do evendo for sair
                    pygame.quit() #CLose Window
                    quit() #encerra a inicialização do pygame
    #Formatação texto
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)