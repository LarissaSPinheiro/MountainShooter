#!/usr/bin/python
# Classe abstrata. Todos os métodos somente serão implementados pelos seus filhos
from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple): #posição do objeto (imagem) onde ele precisa aparecer na tela
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha() #busca as imagens de forma dinâmica. Converte trata a imagem de maneira otimizada
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  #cria o retângulo em volta da imagem de forma dinâmica
        self.speed = 0 #Velocidade dos inimigos

    #@ = decoraitor
    @abstractmethod
    def move(self, ):
        pass
