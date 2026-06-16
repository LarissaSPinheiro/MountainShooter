import sys

import pygame

from code.Score import Score
from code.menu import Menu

from code.const import WIN_WIDTH
from code.const import WIN_HEIGHT
from code.const import MENU_OPTION
from code.level import Level

#método para abrir a janela
class Game:
    #chama o construtor pela primeira vez e da um game init
    def __init__(self):
        pygame.init() #inicialização do pygame
        #Para criar uma janela utilizasse a variável window
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT)) #tamanho da janela 600px por 480px

    def run(self, game_mode=None):
        while True:
            score = Score(self.window)
            menu = Menu(self.window) #primeiro chamar o menu
            menu_return = menu.run() #retorna a opção do menu que o usuário clicar
            game_mode = menu_return

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0] #[Player1, Player2]
                level = Level(self.window, 'Level1', menu_return, player_score) #Inicializa objeto da classe level
                level_return = level.run(player_score) #Começar a execução
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:  # exit
                score.show()
            elif menu_return == MENU_OPTION[4]: #exit
                pygame.quit()  # CLose Window
                quit()  # encerra a inicialização do pygame
            else:
                pygame.quit()
                sys.exit()