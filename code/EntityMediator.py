from code.enemy import Enemy
from code.entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity): #para verificar se atingiu o limit da tela, __ privado somente dentro da class
        if isinstance(ent, Enemy):  #verifica se a entidade é do tipo inimigo
            if ent.rect.right < 0:  #quando passar da tela zerar vida inimigo
                ent.health = 0
        pass


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity) #se bater na borda desaparece

    #Verifica vida
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0: #vida menor igual a zero
                entity_list.remove(ent) #remove entidade
