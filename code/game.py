#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.menu import Menu

from code.const import WIN_WIDTH
from code.const import WIN_WEIGHT

#método para abrir a janela
class Game:
    #chama o construtor pela primeira vez e da um game init
    def __init__(self):
        pygame.init() #inicialização do pygame
        #Para criar uma janela utilizasse a variável window
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_WEIGHT)) #tamanho da janela 600px por 480px

    def run(self):
            menu = Menu(self.window) #primeiro chamar o menu
            menu.run()
            pass