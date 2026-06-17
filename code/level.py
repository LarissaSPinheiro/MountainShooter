#Gerencia cada fase. Cria a lista de entidades (background + players + inimigos).
# O while True interno move e desenha tudo, checa colisões via EntityMediator.
# Retorna True (vitória por timeout) ou False (todos os players mortos).
#Métodos: __init__ · run → bool · level_text

import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.EntityMediator import EntityMediator
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory

from code.const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.player import Player

from code.entity import Entity


class Level:
    #Cria a entity_list com backgrounds e players. Configura timers pygame: EVENT_ENEMY (spawn de inimigos a cada 4s) e EVENT_TIMEOUT (contagem regressiva a cada 100ms).
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL #contador da fase
        self.window = window
        self.name = name
        self.game_mode = game_mode #armazena o modo escolido (1P, 2P Coop, 2P Versus)
        self.entity_list: list[Entity] = [] #lista de todos objetos da fase
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg')) #pega os objetos do nivel 1 e joga na lista
        player = EntityFactory.get_entity('Player1') #Inicializa pelo construtor a nave 1
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION [2]]:
            player = EntityFactory.get_entity('Player2')  # Inicializa pelo construtor a nave 1
            player.score = player_score[1]
            self.entity_list.append(player)
        # a CADA X tempo teremos um inimigo
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP) #checa a condição de vitória 100MS


    #Loop da fase. Retorna True se o tempo esgotou (vitória) ou False se todos os players morreram (derrota).
    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3') #Adicionada musica ao Level 1
        pygame.mixer_music.set_volume(0.3) #diminuir volume músicas
        pygame.mixer_music.play(-1) #Executar indefinidamente
        clock = pygame.time.Clock() #Executa conforme um tempo específico
        while True:
            clock.tick(60)  #A cada frame (60x por segundo):
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect) #desenha a imagem em tela
                ent.move() #move os player e enemys
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot() #tenta atirar
                    if shoot is not None:
                        self.entity_list.append(shoot) #adiciona tiro à lista
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
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP #decrementa os 20000 tirando 100
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False

            #printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10 , 5))  # Mostra o tempo de duração da fase
            self.level_text(14, f'fps: {clock.get_fps() :.0f}s', C_WHITE, (10, WIN_HEIGHT - 35))  # Print do clock em tela, imprime o FPS do game
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))  # Depuração do código, demonstra quantas entidades há em tela
            pygame.display.flip() #mostra em tela
            #Colisão
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    #Desenha textos na fase: tempo restante, FPS, vida e pontuação dos players.
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0],top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)