# Estático get_entity que recebe um nome e retorna o objeto correto.
# Centraliza a criação de todas as entidades (backgrounds, players, inimigos),
# separando a lógica de instanciação do restante.

import random
from unittest import case

from pygame.examples.grid import WINDOW_HEIGHT

from code.background import Background
from code.const import WIN_WIDTH
from code.const import WIN_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    #da classe e não do objeto
    @staticmethod
    #Recebe um nome e retorna o objeto correto já instanciado
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7): #level1bg images number
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0))) #busca a imagem de acordo com o laço de repetição
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(5): #level2bg images number
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0))) #busca a imagem de acordo com o laço de repetição
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30)) #Posição do player 1 na
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))  # Posição do player 2 na tela
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10,  random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

