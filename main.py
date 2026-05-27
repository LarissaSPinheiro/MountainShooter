import pygame

print('Setup Star')
pygame.init() #inicialização do pygame

#Para criar uma janela utilizasse a variável window
print('Setup End')
window = pygame.display.set_mode(size = (600, 480)) #tamanho da janela 600px por 480px


print('Loop Star')
#Laço para manter a janela aberta
while True:
    #Criasse o evento para finalizar a janela
    #Check for all events
    for event in pygame.event.get(): #checa e pega os eventos
        if event.type == pygame.QUIT: #se o tipo do evendo for sair
            print('Quitting...')
            pygame.quit() #CLose Window
            quit() #encerra a inicialização do pygame
