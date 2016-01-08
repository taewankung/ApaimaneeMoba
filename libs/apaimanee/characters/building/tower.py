from building import Building
from bge import logic


class Tower(Building):
    def __init__(self,
                 controller,
                 unit,
                 spawn_bullet,
                 enemy_list):
        
        super().__init__(
                        controller,
                        unit,
                        enemy_list
                        )
        self.spawn_bullet = spawn_bullet

    def destroyed(self):
        if self.cont.sensors["Message"].positive :
            self.unit.sendMessage("reward","200",str(self.cont.sensors["Message"].bodies[0]))
            self.unit.sendMessage("destroyed","",str(self.spawn_bullet))
            self.unit.endObject()
            print(str(self.cont.sensors["Message"].bodies))

    def damaged(self):
        if self.cont.sensors["Message"].positive :
            scene = logic.getCurrentScene()
            enemy = scene.objects[str(self.cont.sensors["Message"].bodies[0])]
            self.unit["hp"]=self.unit["hp"]-enemy["dmg"]
           # print(self.unit["hp"])

    def attack(self,damage):#point_spawn = KX_Object
        dist = 0

        if self.cont.sensors["Near"].positive :
            for character in self.cont.sensors["Near"].hitObjectList:
                if character.getDistanceTo(self.unit) < dist or dist == 0:
                    dist = character.getDistanceTo(self.unit)
                    obj = character
                    self.unit.sendMessage("attack",str(obj),str(self.spawn_bullet))
           # self.unit.sendMessage("attack",str(damage),self.cont.sen)
