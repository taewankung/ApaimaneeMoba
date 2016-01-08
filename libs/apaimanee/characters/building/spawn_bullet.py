from bge import logic
import math


class Spawn_bullet:
    def __init__(self,
                unit_spawn,
                bullet,
                time
                ):
                self.unit_spawn = unit_spawn
                self.bullet = bullet
                self.cont = self.unit_spawn.controllers["Python"]
                self.scene = logic.getCurrentScene()
                self.time = time
                 
    def spawn(self):
        message = self.cont.sensors["Message"]
        spawn_act = self.cont.actuators["spawn"]
        if message.positive :
            track = self.cont.actuators["Track"]
            track.object = self.scene.objects[message.bodies[0]]
            #self.unit_spawn["time"]=self.unit_spawn["time"]+0.01
            self.cont.deactivate(spawn_act)
            self.cont.activate(track)
            #print( math.fabs(self.unit_spawn["time"]-0.9 ))
            if math.fabs(self.unit_spawn["time"]-(self.time+0.9)) < 9e-1:
                self.unit_spawn["time"] = 0e-16 
                spawn_act.object = "bullet"
                self.cont.activate(spawn_act)
        if self.unit_spawn["time"] > self.time:
            self.unit_spawn["time"] = 0e-16
                

    def check_destroy(self):
        destroyed_mes = self.cont.sensors["destroyed"] 
        if destroyed_mes.positive:
            self.unit_spawn.endObject()
