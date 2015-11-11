from bge import logic
from ApaimaneeMoba.lib.characters.GameUnit import GameUnit


class Building(GameUnit):
    
    def __init__(self, name, max__hp,armor, building_team):
        super().__init__(self,name,max_hp)
        self,building_team = building_team
    
    def attack(self,damaged):
        pass
    

