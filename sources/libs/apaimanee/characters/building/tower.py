from building import Building
import uuid
import bge


class Tower(Building):
    def __init__(self,
                 owner,
                 spawn_bullet=""
                 ):
        
        super().__init__(owner)
        
        self.spawn_bullet = spawn_bullet

    def destroyed(self):
        if self.controller.sensors["Message"].positive :
            self.sendMessage("reward","200",str(self.controller.sensors["Message"].bodies[0]))
            self.sendMessage("destroyed","",str(self.spawn_bullet))
            self.endObject()

    def attack(self):
        if self.controller.sensors["Near"].positive :
            dist =0
            obj = None
            for character in self.controller.sensors["Near"].hitObjectList:
                if character["team"] != self["team"]:
                    if character.getDistanceTo(self) < dist or dist == 0:
                        dist = character.getDistanceTo(self)
                        obj = character
                        self.sendMessage("attack",str(obj),str(self.spawn_bullet))
                        return obj
