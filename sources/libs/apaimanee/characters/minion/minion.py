from bge import logic
from libs.apaimanee.characters.GameUnit import GameUnit
import math

import uuid


class Minion(GameUnit):
    def __init__(self, 
                 controller,
                 skeleton_name,
                 creep_action,):
        super().__init__(controller)

        #self.checkpoint = checkpoint
        self.track = self.controller.actuators["track"]
        self.animation = self.controller.actuators["animation"]
        self.near = self.controller.sensors["Near"]
        self.col_enemy = self.controller.sensors["col_enemy"]
        self.move = self.controller.actuators["Move"]
        self.attack_act = self.controller.actuators["attack_mes"]
        self.scene = logic.getCurrentScene()        
        self.skeleton_name = skeleton_name
        self.creep_action = creep_action
    
    def set_first_path(self,first_path):
        if self.owner["init"] == 0 :
            self.owner["mem_path"] = first_path 
            self.owner["init"]=1

    def move_unit(self):
        self.track.object = self.scene.objects[self.owner["mem_path"]]
        self.controller.activate(self.track)
        if self.controller.sensors["col_path"].positive :
            self.track.object = self.controller.sensors["col_path"].hitObject["path"]
            self.owner["mem_path"]= self.controller.sensors["col_path"].hitObject["path"]
        
        if self.near.positive:
            hit_objs = self.near.hitObjectList
            dist = 0
            obj = None
            count = 0
            for item in hit_objs:
                if "team" in item:
                    if item["team"] != self.owner["team"]:
                        if item.getDistanceTo(self.owner) < dist or dist ==0:
                            dist = item.getDistanceTo(self.owner)
                            obj = item
                            self.track.object = obj
                            self.controller.activate(self.move)
                            self.controller.activate(self.track)
                            self.owner["states"]="move"

                            if self.col_enemy.positive:
                                self.controller.deactivate(self.move)
                                self.attack(obj)
                                self.owner["states"]="attack"
                    if item["team"] == self.owner["team"]:
                        count = count+1
                    if count == len(hit_objs):
                        self.owner["states"]="move"
        
        if self.owner["states"]=="move":
            self.controller.activate(self.track)
            self.controller.activate(self.move)
            for bone in self.owner.children:    
                if bone.name == self.skeleton_name:
                    bone.playAction(self.creep_action,
                                     10,68,
                                     play_mode = logic.KX_ACTION_MODE_PLAY,
                                     speed=1)
    
    def attack(self,enemy):
        for bone in self.owner.children:
            if bone.name == self.skeleton_name:
                bone.playAction(self.creep_action,
                                          90,117.0000000000000000000000000000,
                                          play_mode = logic.KX_ACTION_MODE_PLAY,
                                          speed=1)
                if math.fabs(bone.getActionFrame()-117)< 99e-2 :
                    bone.stopAction()
                    self.owner.sendMessage("attack",self.owner.name,str(enemy))
                    self.owner.sendMessage("attack_unitID",enemy["id"],str(enemy))
     
    def die_and_gold(self):
        if self.controller.sensors["Message"].positive:
            enemy = self.controller.sensors["Message"].bodies[0]
            self.owner.sendMessage("reward","90",enemy)
            self.owner.endObject()
            pass
