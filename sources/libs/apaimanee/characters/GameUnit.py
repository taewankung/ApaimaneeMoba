from bge import logic
import uuid

class GameUnit:
    def __init__(self
                 ):
        self.id = str(uuid.uuid4())
        self.controller = logic.getCurrentController()
        self.owner = controller.owner

       
    def reduce_hp(self, damaged):
        self.owner["hp"] = damaged*((100-self.owner["armor"])/100)

    def regend_hp(self,hp):
        self.owner["hp"] += hp

    def die(self):
        self.owner["alive"] = False

    def get_alive(self):
        self.owner["alive"] = True
    #///////////////////// Interface ////////////////////////
    def move_unit(self):
        pass
    #//////////////////// Interface /////////////////////////
    def attack(self):
        pass
    
    def get_owner(self):
        return self.owner

    def show_status(self):
        print("Name: ", self.owner["name"])
        print("hp: ", self.owner["hp"])
        print("id: ",id(self.owner))
        if(self.owner["alive"] == False ):
           print("alive status: Die")
        else:
           print("alive status: Alive")
    
    def damaged(self):
        scene = logic.getCurrentScene()
        obj = None
        if self.controller.sensors["Message"].positive and self.controller.sensors["id_message"].positive:
            enemy = self.controller.sensors["Message"].bodies[0]
            #print(enemy)#enemy attack
            id_mine = self.controller.sensors["id_message"].bodies[0]
            if self.controller.sensors["id_message"].bodies[0] == self.owner["id"]:
                if enemy in scene.objects:
                    obj = scene.objects[enemy]#
                if self.owner["id"] == id_mine:
                    #print("yes")
                    if "hp" in self.owner and "hp" in obj:
                        if self.owner["hp"] > 0:
                            self.owner["hp"] = self.owner["hp"]-float(obj["dmg"])
