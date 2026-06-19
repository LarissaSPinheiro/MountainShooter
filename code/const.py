#Todas as constantes do jogo: tamanhos de janela, velocidade/vida/dano/score de cada entidade,
# teclas dos players, eventos customizados do pygame, opções de menu e posições da tela de score.

import pygame

#C
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 251, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

#velocidade em pixels por frame.
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Fish1': 3,
    'Fish1Shot': 1,
    'Fish2': 3,
    'Fish2Shot': 3,
    'Shark': 1, #inimigo 1
    'SharkShot': 5,
    'Octopus': 1, #inimigo 2
    'OctopusShot': 2,
}

#Vida Inicial. Backgrounds possuem vidas imortais
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Fish1': 300,
    'Fish1Shot': 1,
    'Fish2': 300,
    'Fish2Shot': 1,
    'Shark': 50,
    'SharkShot': 1,
    'Octopus': 60,
    'OctopusShot': 1,
}

ENTITY_SHOT_DELAY = {
    'Fish1': 20,
    'Fish2': 15,
    'Shark': 100,
    'Octopus': 200,
}

# Dano Causado ao colidir. Background dano zero
ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Fish1': 1,
    'Fish1Shot': 25,
    'Fish2': 1,
    'Fish2Shot': 20,
    'Shark': 1,
    'SharkShot': 20,
    'Octopus': 1,
    'OctopusShot': 15,
}

#Pontos que o player ganha ao destruir uma entidade
ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Fish1': 0,
    'Fish1Shot': 0,
    'Fish2': 0,
    'Fish2Shot': 0,
    'Shark': 100,
    'SharkShot': 0,
    'Octopus': 125,
    'OctopusShot': 0,
}

#G
GRAVITY = 0.5

# J
JUMP_FORCE = -10

# M
#Opções do menu
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT'
)

# P

#Permite adicionar novos players sem mudar o codigo de movimento
PLAYER_KEY_UP = {'Fish1': pygame.K_UP,
                 'Fish2': pygame.K_w}
PLAYER_KEY_DOWN = {'Fish1': pygame.K_DOWN,
                 'Fish2': pygame.K_s}
PLAYER_KEY_LEFT = {'Fish1': pygame.K_LEFT,
                 'Fish2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Fish1': pygame.K_RIGHT,
                 'Fish2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Fish1': pygame.K_SPACE,
                 'Fish2': pygame.K_LCTRL
                    }
# S
SPAWN_TIME = 4000


# T

TIMEOUT_STEP = 100 #100ms
TIMEOUT_LEVEL = 20000 #20s


# W

#Tamanho da janela em pixels
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 90),
    'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230),
    7: (WIN_WIDTH / 2, 250),
    8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}