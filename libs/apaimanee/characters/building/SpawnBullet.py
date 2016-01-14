from bge import logic
from libs.apaimanee.characters.SpawnUnit import SpawnUnit
import math


class SpawnBullet:
    def __init__(self,
                unit_spawn,
                controller,
                bullet,
                time
                ):
                self.unit_spawn = unit_spawn
                self.bullet = bullet
                self.cont = controller
                self.scene = logic.getCurrentScene()
                self.time = time
    def track(self,traget):
        track = self.cont.actuators["Track"]
        if str(traget) in self.scene.objects:
            track.object = traget
                     
    def spawn(self):
        track = self.cont.actuators["Track"]
        message_sen = self.cont.sensors["Message"]
        spawn_act = self.cont.actuators["spawn"]
        send_msg_bullet = self.cont.actuators["Message"]
        #print(message_sen.bodies[0])
        if message_sen.positive :
            send_msg_bullet.body = str(track.object)
            #self.unit_spawn["time"]=self.unit_spawn["time"]+0.01
            self.cont.deactivate(spawn_act)
            self.cont.activate(send_msg_bullet)
            self.cont.activate(track)
            #print( math.fabs(self.unit_spawn["time"]-0.9 ))
            if math.fabs(self.unit_spawn["time"]-(self.time+0.9)) < 9e-1:
                self.unit_spawn["time"] = 0e-16
                #print("spawn") 
                spawn_act.object = "bullet"
                self.cont.activate(spawn_act) 
        if self.unit_spawn["time"] > self.time:
            self.unit_spawn["time"] = 0e-16

    def up_time(self):
        self.time = self.time + 5
                
    def check_destroy(self):
        destroyed_mes = self.cont.sensors["destroyed"] 
        if destroyed_mes.positive:
            self.unit_spawn.endObject()
