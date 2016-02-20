import bge
import uuid

class GameObject(bge.types.KX_GameObject):
    def __init__(self, owner):
        self.id = str(uuid.uuid4())
        self.controller = bge.logic.getCurrentController()
        self.hp = 200

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
        print("Name: ", self["unit_name"])
        print("hp: ", self["hp"])
        print("id: ",id(self))
        if(self["alive"] == False ):
           print("alive status: Die")
        else:
           print("alive status: Alive")

    def damaged(self):
        scene = bge.logic.getCurrentScene()
        obj = None
        if self.controller.sensors["Message"].positive and self.controller.sensors["IdMessage"].positive:
            enemy = self.controller.sensors["Message"].bodies[0]
            id_message_sensor_body = self.controller.sensors["IdMessage"].bodies[0]
            if id_message_sensor_body == self.id:
                if enemy in scene.objects:
                    obj_enemy_in_scene = scene.objects[enemy]#
                if self.id == id_message_sensor_body:
                    #print("yes")
                    if "hp" in self and "hp" in obj_enemy_in_scene:
                        if self["hp"] > 0:
                            self["hp"] = self["hp"]-float(obj_enemy_in_scene["dmg"])
                            self.hp = self.hp - float(obj_enemy_in_scene["dmg"])
                            print(self.hp)
                        else:
                            self.die()

