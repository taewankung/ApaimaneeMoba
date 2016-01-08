from bge import logic


class Bullet:
    def __init__(self,
                 unit
                ):
        self.unit = unit
        self.cont = logic.getCurrentController()
    def attack(self):
        #print(self.unit.name)
        self.cont.activate(self.cont.actuators["Motion"])
        if self.cont.sensors["Collision"].positive :
            self.unit.sendMessage("reduce_hp",)
            self.unit.endObject() 
