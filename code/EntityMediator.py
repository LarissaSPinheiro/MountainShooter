#Detecta colisões entre entidades, verifica se saíram da tela e distribui pontuação.
# Usa isinstance para saber quem pode colidir com quem (ex: PlayerShot só colide com Enemy).
#isinstance() é uma função Python que verifica se um objeto é de uma classe específica. isinstance(ent, Enemy)
# retorna True se ent for um Enemy (ou subclasse). É como perguntar "esse objeto é um inimigo?"

from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.const import WIN_WIDTH
from code.enemy import Enemy
from code.entity import Entity
from code.player import Player


class EntityMediator:

    @staticmethod
    #Remove entidades que saíram da tela: inimigos que passaram pela esquerda, tiros que saíram pelos lados.
    def __verify_collision_window(ent: Entity): #para verificar se atingiu o limit da tela, __ privado somente dentro da class
        if isinstance(ent, Enemy):  #verifica se a entidade é do tipo inimigo
            if ent.rect.right <= 0:  #quando passar da tela zerar vida inimigo
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):  #verifica se a entidade é do tipo inimigo
            if ent.rect.right <= 0:  #destruição do tiro
                ent.health = 0

    @staticmethod
    #Compara cada par de entidades. Para cada par válido (Enemy+PlayerShot ou Player+EnemyShot), verifica sobreposição de rects. Se colidir, aplica dano mútuo.
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction: # if valid_interaction == True
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name #para pontar no scoure
                ent2.last_dmg = ent1.name #para pontar no scoure


    @staticmethod
    # privado (__). Olha enemy.last_dmg para saber qual player atirou e adiciona os pontos ao score dele.
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Fish1Shot':
            for ent in entity_list:
                if ent.name == 'Fish1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Fish2Shot':
            for ent in entity_list:
                if ent.name == 'Fish2':
                    ent.score += enemy.score

    @staticmethod
    #Compara cada par de entidades. Para cada par válido (Enemy+PlayerShot ou Player+EnemyShot), verifica sobreposição de rects. Se colidir, aplica dano mútuo.
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1) #se bater na borda desaparece
            for j in range(i+1, len(entity_list)): #laço tamanho da entidade para comparar coma entidade1
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    #Percorre a lista e remove entidades com health <= 0. Se for um Enemy, chama __give_score antes de remover.
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0: #vida menor igual a zero
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent) #remove entidade

    #Vefica se o jogador está em cima de uma plataforma
    @staticmethod
    def verify_platform(player, platforms):
        player.on_ground = False #reseta antes de checar
        for plat in platforms:
            if (player.vel_y > 0 and
                    player.rect.bottom >= plat.rect.top and
                    player.rect.bottom <= plat.rect.top + 10 and
                    player.rect.right > plat.rect.left and
                    player.rect.left < plat.rect.right):
                    player.rect.bottom = plat.rect.top
                    player.vel_y = 0
                    player.on_ground = True
