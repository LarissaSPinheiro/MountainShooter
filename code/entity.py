#Classe abstrata (ABC) para todas as entidades do jogo.
# Define atributos comuns: surf, rect, health, damage, score.
# O move é abstrato — cada filho implementa o próprio movimento.

from abc import ABC, abstractmethod

import pygame

from code.const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    #Carrega a imagem PNG com base no name, cria o rect na posição indicada, e busca vida/dano/score em const.py.

    def __init__(self, name: str, position: tuple): #posição do objeto (imagem) onde ele precisa aparecer na tela
        self.name = name #Nome da entidade (ex: "Player1", "Enemy1"). Usado para carregar a imagem e buscar valores em const.py.
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha() #busca as imagens de forma dinâmica. Converte trata a imagem de maneira otimizada
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  #cria o retângulo em volta da imagem de forma dinâmica
        self.speed = 0 #Velocidade dos inimigos
        self.health = ENTITY_HEALTH[self.name] #vida do player ou inimigo
        self.damage = ENTITY_DAMAGE[self.name] #Dano causado ao colidir com outra entidade
        self.score = ENTITY_SCORE[self.name] #pontos que o player ganha ao destruir esta entidade
        self.last_dmg = 'None' #Nome da entidade que causou o último dano. Usado para saber qual player pontua

    #Cada filho DEVE implementar este. O Python lança erro se tentar criar um filho que não implemente move().
    @abstractmethod # é um "contrato". Ao colocar esse decorador em move(), você garante que nenhuma subclasse esquece de implementar o movimento. Python vai reclamar em tempo de execução se tentar instanciar uma classe sem ele.
    def move(self):
        pass