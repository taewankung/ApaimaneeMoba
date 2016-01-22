from bge import logic
from libs.apaimanee.characters.GameUnit import GameUnit
import math

class Minion(GameUnit):
    def __init__(self, 
                 #checkpoint,
                 controller,
                 animation,
                 unit,
                 team_enemy,
                 skeleton_name,
                 creep_action,
                 enemy_list=[]):
        super().__init__(
                        controller,
                        unit,
                        enemy_list,
                        )
        #self.checkpoint = checkpoint
        self.team_enemy =team_enemy
        self.track = self.cont.actuators["track"]
        self.animation = self.cont.actuators["animation"]
        self.near = self.cont.sensors["Near"]
        self.col_enemy = self.cont.sensors["col_enemy"]
        self.move = self.cont.actuators["Move"]
        self.attack_act = self.cont.actuators["attack_mes"]
        self.scene = logic.getCurrentScene()        
        self.skeleton_name = skeleton_name
        self.creep_action = creep_action

    def get_gold(self, gold, hero):
        pass
    def set_team(self):
        if self.team_enemy == "team2":
#            self.col_enemy.propName = "team2"
            self.near.propName = "team2"
        elif self.team_enemy == "team1":
#            self.col_enemy.propName = "team1"
            self.near.propName = "team1"
    
    def set_first_path(self,first_path):
        if self.unit["init"] == 0 :
            self.unit["mem_path"] = first_path 
            self.unit["init"]=1

    def move_unit(self):
        self.track.object = self.scene.objects[self.unit["mem_path"]]
        self.cont.activate(self.track)
        if self.cont.sensors["col_path"].positive :
            self.track.object = self.cont.sensors["col_path"].hitObject["path"]
            self.unit["mem_path"]= self.cont.sensors["col_path"].hitObject["path"]
        
        if self.near.positive:
            hit_objs = self.near.hitObjectList
            dist = 0
            obj = None
            for item in hit_objs:
                if item.getDistanceTo(self.unit) < dist or dist ==0:
                    dist = item.getDistanceTo(self.unit)
                    obj = item
                    if obj.getDistanceTo(self.unit)>0 and obj.getDistanceTo(self.unit)<2:
                        self.move.dLoc=[0,-0.2,0]
                        self.cont.activate(self.move)
                    if obj.getDistanceTo(self.unit)>0 and obj.getDistanceTo(self.unit)<10:
                        self.cont.deactivate(self.move)
                        self.attack(obj)

            self.track.object = obj
            self.cont.activate(self.track)
        
        #if self.col_enemy.positive :
            #self.move.dLoc =[1,-1,0]
            #self.cont.deactivate(self.move)
            #self.attack()
            #print("attack")
        else:
            #self.cont.deactivate(self.attack_act)
            self.cont.activate(self.move)
            for bone in self.unit.children:    
                if bone.name == self.skeleton_name:
                    bone.playAction(self.creep_action,
                                     10,68,
                                     play_mode = logic.KX_ACTION_MODE_PLAY,
                                     speed=1)
    
    def attack(self,enemy):
        for bone in self.unit.children:
            if bone.name == self.skeleton_name:
                bone.playAction(self.creep_action,
                                          90,117.0000000000000000000000000000,
                                          play_mode = logic.KX_ACTION_MODE_PLAY,
                                          speed=1)
                if math.fabs(bone.getActionFrame()-117)< 99e-2 :
                    bone.stopAction()
                    self.unit.sendMessage("attack",self.unit.name,str(enemy))
                    self.unit.sendMessage("attack_unitID",str(id(enemy)),str(enemy))
     
    def die_get_gold(self):
        if self.cont.sensors["Message"].positive :
            enemy = self.cont.sensors["Message"].bodies[0]            
            if self.unit["hp"] <=0:
                self.SendMessage("reward","90",enemy)
                self.unit.endObject()
                pass
