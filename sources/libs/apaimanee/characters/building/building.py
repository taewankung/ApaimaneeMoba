from bge import logic
from libs.apaimanee.characters.game_object import GameObject

class Building(GameObject):
    def __init__(self, owner):
        super().__init__(owner)
        #self,building_team = building_team
    
    def attack(self,damaged):
        pass

    def destroyed(self):
        if self.controller.sensors["Message"].positive:
            self.sendMessage("reward","100",str(self.controller.sensors["Message"].bodies[0]))
            self.endObject()
