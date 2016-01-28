import bge
import uuid

class GameObject(bge.types.KX_GameObject):
    def __init__(self, owner):
        self.id = str(uuid.uuid4())
        self.controller = bge.logic.getCurrentController()

       
    def reduce_hp(self, damaged):
        self["hp"] = damaged*((100-self["armor"])/100)

    def regend_hp(self,hp):
        self["hp"] += hp

    def die(self):
        self["alive"] = False

    def get_alive(self):
        self["alive"] = True
    #///////////////////// Interface ////////////////////////
    def move_unit(self):
        pass
    #//////////////////// Interface /////////////////////////
    def attack(self):
        pass
    
    def get_owner(self):
        return self

    def show_status(self):
        print("Name: ", self["name"])
        print("hp: ", self["hp"])
        print("id: ",id(self))
        if(self["alive"] == False ):
           print("alive status: Die")
        else:
           print("alive status: Alive")
    
    def damaged(self):
        scene = bge.logic.getCurrentScene()
        obj = None
        if self.controller.sensors["Message"].positive and self.controller.sensors["id_message"].positive:
            enemy = self.controller.sensors["Message"].bodies[0]
            #print(enemy)#enemy attack
            id_mine = self.controller.sensors["id_message"].bodies[0]
            if self.controller.sensors["id_message"].bodies[0] == self["id"]:
                if enemy in scene.objects:
                    obj = scene.objects[enemy]#
                if self["id"] == id_mine:
                    #print("yes")
                    if "hp" in self and "hp" in obj:
                        if self["hp"] > 0:
                            self["hp"] = self["hp"]-float(obj["dmg"])
