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
        collision =  self.cont.sensors["Collision"]
        if collision.positive :
            #print(collision.hitObject)
            #print(hit_obj)
            if  message.positive :
                if "hp" in collision.hitObject:
                    collision.hitObject["hp"] = collision.hitObject["hp"]-damage
                #print(message.bodies[0])
#                self.unit.sendMessage("reduce_hp",str(damage),str(collision.hitObject))
            self.unit.endObject()
        if self.cont.sensors["Collision_ground"].positive :
            self.unit.endObject()
