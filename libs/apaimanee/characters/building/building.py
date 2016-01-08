from bge import logic
from libs.apaimanee.characters.game_unit import GameUnit

class Building(GameUnit):
    
    def __init__(self, controller,unit,enemy_list):
        super().__init__(controller,
                         unit,
                         enemy_list)
        #self,building_team = building_team
    
    def attack(self,damaged):
        pass
    

