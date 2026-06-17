#Exibe a tela inicial com as opções (1P, 2P Coop, 2P Versus, Score, Exit).
# Captura as teclas ↑ ↓ e Enter para navegar e retorna a opção escolhida como string.
#Métodos: run → retorna string da opção · menu_text

import pygame

from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH
from code.const import C_ORANGE
from code.const import C_WHITE
from code.const import C_YELLOW
from code.const import MENU_OPTION


class Menu:

    def __init__(self, window):
        self.window = window #Referência à janela do jogo para desenhar o menu nela.
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha() #A imagem de fundo do menu (MenuBg.png).
        self.rect = self.surf.get_rect(left=0, top=0) #cria o retângulo

    #Loop do menu. Escuta teclas ↑ ↓ Enter. Retorna a string da opção escolhida. A opção atual fica amarela; as outras ficam brancas.
    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/menu.mp3') #carrega a música
        pygame.mixer_music.play(-1) #toca a música (-1 continua tocando)

        while True:
            #DRAW IMAGENS
            self.window.blit(source=self.surf, dest=self.rect)  # Adicionando a imagem ao retângulo
            self.menu_text(50, "Mountain", (C_ORANGE), ((WIN_WIDTH / 2), 70)) #Adiciona texto ao menu
            self.menu_text(50, "Shooter", (C_ORANGE), ((WIN_WIDTH / 2), 120)) #Adiciona texto ao menu

            #Cria o laço de repetição das opções do menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option: #Adiciona a cor amarela para o menu que está selecionado
                    self.menu_text(20, MENU_OPTION[i], (C_YELLOW), ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], (C_WHITE), ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            #Criasse o evento para finalizar a janela / #Check for all events
            for event in pygame.event.get(): #checa e pega os eventos
                if event.type == pygame.QUIT: #se o tipo do evendo for sair
                    pygame.quit() #CLose Window
                    quit() #encerra a inicialização do pygame
                #Adicionar seleção de menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #telha para baixo
                        if menu_option < len(MENU_OPTION) - 1: #incrementa para retornar a primeira opção após chegar na última
                            menu_option += 1 #incremanta conforme seta para baixo
                        else:
                            menu_option = 0 #Retona para o começo
                    if event.key == pygame.K_UP: #telha para cima
                        if menu_option > 0: #
                            menu_option -= 1 #decremanta conforme seta para cima
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #Enter
                        return MENU_OPTION[menu_option] #para retornar o nome da opção corretamente


    #Renderiza um texto na posição indicada. Usada para desenhar o título e cada opção do menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)