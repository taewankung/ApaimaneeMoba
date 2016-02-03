import bge 
from libs.apaimanee.characters.spawn_unit import SpawnUnit
import math
import uuid


class SpawnBullet(bge.types.KX_GameObject):
    def __init__(self,
                owner,
                bullet,
                time
                ):

                self.id = str(uuid.uuid4())
                self.cont = bge.logic.getCurrentController()
                self.bullet = bullet
                self.time = time
                self.current_scene = bge.logic.getCurrentScene()
    
    def track(self,traget):
        track = self.cont.actuators["Track"]
        if str(traget) in self.current_scene.objects:
            track.object = traget
        self.spawn(traget)
                     
    def spawn(self,traget):
        track = self.cont.actuators["Track"]
        message_sen = self.cont.sensors["Message"]
        spawn_act = self.cont.actuators["Spawn"]
        send_msg_bullet = self.cont.actuators["Message"]
        #print(message_sen.bodies[0])
        if message_sen.positive :
            #send_msg_bullet.body = str(track.object)
            #self["time"]=self["time"]+0.01
            self.cont.deactivate(spawn_act)
            self.cont.activate(send_msg_bullet)
            self.cont.activate(track)
            #print( math.fabs(self["time"]-0.9 ))
            if math.fabs(self["time"]-(self.time+0.9)) < 9e-1:
                self["time"] = 0e-16
                #print("spawn")
                send_msg_bullet.body = self["tower"]
                spawn_act.object = "bullet"
                self.cont.activate(spawn_act) 
            if self["time"] > self.time:
                self["time"] = 0e-16
            if "bullet" in self.current_scene.objects:
                bullet = self.current_scene.objects["bullet"]
                bullet["tower"] = self["tower"]
            
                
    def check_destroy(self):
        destroyed_mes = self.cont.sensors["Destroyed"] 
        if destroyed_mes.positive:
            self.endObject()
