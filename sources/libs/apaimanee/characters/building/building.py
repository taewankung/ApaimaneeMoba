from bge import logic
from libs.apaimanee.characters.game_object import GameObject

class Building(GameObject):
    
    def __init__(self, owner):
        super().__init__(owner)
        #self,building_team = building_team
    
    def attack(self,damaged):
        pass
