#Tela de placar. save coleta o nome do jogador e grava no banco. show exibe o top 10.
# O ESC no show executa return, voltando ao loop do Game.
#Métodos: save · show · score_text

import datetime
import sys


import pygame
from pygame import Rect, Surface, K_RETURN, K_BACKSPACE, K_DOWN, KEYDOWN, K_ESCAPE
from pygame.font import Font

from code.DBProxy import DBProxy
from code.const import C_YELLOW, SCORE_POS, MENU_OPTION, C_WHITE


class Score:
    #construtor
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()  # carregando a imagem. Convert adicionado para melhorar a dimensão da imagem
        self.rect = self.surf.get_rect(left=0, top=0)  # cria o retângulo
        pass

    #Exibe "YOU WIN!!", coleta um nome de 4 caracteres via teclado, calcula a pontuação final de acordo com o modo de jogo e grava no banco. Depois chama show() automaticamente.
    def save(self, game_mode:str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')  # carrega a música
        pygame.mixer_music.play(-1)  # toca a música (-1 continua tocando)
        db_proxy = DBProxy('DBScore') #abre a conexão com o banco
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', C_YELLOW, SCORE_POS['Title'])
            text = 'Enter Player 1 name (4 character)'
            score = player_score[0]
            # Cálculo da pontuação varia por modo:
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]  # só Player1
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2 # média dos dois
                text = 'Enter team name (4 character)'
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0] #maior pontuação
                    text = 'Enter Player 1 name (4 character)'
                else:
                    score = player_score[1]  # Soma da pontuação dos dois jogadores
                    text = 'Enter Player 2 name (4 character)'
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()}) #salva no banco
                        self.show() #implementa enter para ver o score
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                        score = 0
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    #Busca o top 10 no banco via DBProxy e exibe na tela. Fica em loop até ESC ser pressionado, quando retorna para o Game.
    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')  # carrega a música
        pygame.mixer_music.play(-1)  # toca a música (-1 continua tocando)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME    SCORE    DATE    ', C_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}   {score :05d}  {date}', C_YELLOW, SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()


    # Renderiza um texto na tela de score. Mesma função auxiliar usada pelo Menu.
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

# é uma função fora da classe que retorna a data e hora atual formatada.
def get_formatted_date():
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.strftime("%H:%M%p")
    current_date = current_datetime.strftime("%d/%m/%Y")
    return f"{current_time} - {current_date}"