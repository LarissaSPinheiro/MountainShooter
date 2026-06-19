#Player: lê teclas pressionadas, move nas 4 direções dentro da tela, atira com delay.

import pygame.key

from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY, GRAVITY, JUMP_FORCE
from code.entity import Entity
from code.PlayerShot import PlayerShot

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position) #herda da classe pai
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.score = 0 #pontuação acumulada do player
        self.vel_y = 0 #velocidade atual
        self.on_ground = False #pisando em algo?

    #Movimento de acordo com as teclas (setas) pressionadas
    def move(self):
        #Pulo - só funciona se estiver no chão
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.on_ground:
            self.vel_y = JUMP_FORCE
            self.on_ground = False

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # Se tecla para esquerda
            self.rect.centerx -= ENTITY_SPEED[self.name]  #Altera para o lado esquerdo

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:  # Se tecla para direita
            self.rect.centerx += ENTITY_SPEED[self.name]  #Altera para baixo a posição do player
        # gravidade - puxa para baixo o frame
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Não cai além do final da tela
        if self.rect.bottom >= WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT
            self.vel_y = 0
            self.on_ground = True

    #Limita a quantidade de tiros por segundo o player pode disparar
    def shoot(self):
        self.shot_delay -= 1 #contador de frames até o próximo tiro
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name] #reseta
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery)) #cria o tiro
            else:
                return None
        else:
            return None