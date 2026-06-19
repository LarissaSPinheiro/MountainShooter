import pygame

class Platform:
    def __init__(self, x, y, width):
        self.surf = pygame.image.load('./asset/Platform.png')
        self.surf = pygame.transform.scale(self.surf, (width, 20))
        self.rect = self.surf.get_rect(left=x, top=y)

    def move (self):
        pass #plataformas paradas
