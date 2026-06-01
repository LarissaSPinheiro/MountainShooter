#!/usr/bin/python
# Responsável por gerar as entidades relacionadas. O level aciona a fábrica e ela na linha de montagem gera um produto background, enemy, player
from unittest import case

from code.background import Background
from code.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0))) #busca a imagem de acordo com o laço de repetição
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
