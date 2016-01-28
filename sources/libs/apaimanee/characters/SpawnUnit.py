from bge import logic
import uuid
import math

class SpawnUnit:
    def __init__(self, spawner, unit):
        self.id = str(uuid.uuid4())
        self.spawner = spawner
        self.unit = unit
        self.cont = self.spawner.controllers["Python"]

    def spawn(self,time):
        spawn_act = self.cont.actuators["spawn"]
        #print("spawn")
        if math.fabs(self.spawner["time"]-(time+0.9)) < 9e-1:
            spawn_act.object = self.unit
            self.cont.activate(spawn_act) 
            self.spawner["time"] = 0e-9
            
    def reset(self,time):
        if math.fabs(self.spawner["time"]-(time+0.9)) < 9e-1:
            self.spawner["time"] = 0e-9
        pass
    
    def last_spawn_object(self):
        return self.cont.actuators["spawn"].objectLastCreated
