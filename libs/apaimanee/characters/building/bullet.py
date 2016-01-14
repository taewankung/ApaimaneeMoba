from bge import logic


class Bullet:
    def __init__(self,
                 unit
                ):
        self.unit = unit
        self.cont = logic.getCurrentController()
    
    def attack(self,damage):
        self.cont.activate(self.cont.actuators["Motion"])
        message = self.cont.sensors["Message"]
        if self.cont.sensors["Collision"].positive :
            hit_obj =  self.cont.sensors["Collision"].hitObject
            print(hit_obj)
            #if  message.positive :
             #   self.unit.sendMessage("reduce_hp",str(damage),hit_obj)
            self.unit.endObject()
        elif self.cont.sensors["Collision_ground"].positive :
            self.unit.endObjects()
             
