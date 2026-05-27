#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.menu import Menu


#método para abrir a janela
class Game:
    #chama o construtor pela primeira vez e da um game init
    def __init__(self):
        pygame.init() #inicialização do pygame
        #Para criar uma janela utilizasse a variável window
        self.window = pygame.display.set_mode(size = (600, 480)) #tamanho da janela 600px por 480px

    def run(self):
        while True:  #Laço para manter a janela aberta
            menu = Menu(self.window) #primeiro chamar o menu
            menu.run()
            pass

            #Criasse o evento para finalizar a janela / #Check for all events
            #for event in pygame.event.get(): #checa e pega os eventos
            #    if event.type == pygame.QUIT: #se o tipo do evendo for sair
            #        pygame.quit() #CLose Window
            #        quit() #encerra a inicialização do pygame
