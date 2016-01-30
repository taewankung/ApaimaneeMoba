import bge
from libs.apaimanee.characters.game_object import GameObject
import math

import uuid


class Minion(GameObject):
    def __init__(self, 
                 owner,
                 skeleton_name,
                 creep_action):
        super().__init__(owner)

        self.track = self.controller.actuators["track"]
        self.animation = self.controller.actuators["animation"]
        self.near = self.controller.sensors["Near"]
        self.col_enemy = self.controller.sensors["col_enemy"]
        self.move = self.controller.actuators["Move"]
        self.attack_act = self.controller.actuators["attack_mes"]
        # self.scene = bge.logic.getCurrentScene()        
        self.skeleton_name = skeleton_name
        self.creep_action = creep_action
    
    def set_first_path(self,first_path):
        if self["init"] == 0 :
            self["mem_path"] = first_path 
            self["init"]=1

    def move_unit(self):
        self.track.object = self.scene.objects[self["mem_path"]]
        self.controller.activate(self.track)
        if self.controller.sensors["col_path"].positive :
            self.track.object = self.controller.sensors["col_path"].hitObject["path"]
            self["mem_path"]= self.controller.sensors["col_path"].hitObject["path"]
        
        if self.near.positive:
            hit_objs = self.near.hitObjectList
            dist = 0
            obj = None
            count = 0
            for item in hit_objs:
                if "team" in item:
                    if item["team"]!=self["team"]:
                        if (item.getDistanceTo(self) < dist or dist ==0) :
                            dist = item.getDistanceTo(self)
                            self.track.object = item
                            obj = item
                            #self.controller.activate(self.move)
                            self.controller.activate(self.track)
                            self["states"]="move"
                            if self.col_enemy.hitObject != None and self.col_enemy.hitObject["team"]!=self["team"]:
                                self.controller.deactivate(self.move)
                                #print(type(item))
                                self["states"]="attack"
                                if self["states"]=="attack":
                                    self.attack(obj)

                    if item["team"] == self["team"]:
                        count = count+1
                    if count == len(hit_objs):
                        self["states"]="move"
        
        if self["states"]=="move":
            self.controller.activate(self.track)
            self.controller.activate(self.move)
            for bone in self.children: 
                if bone.name == self.skeleton_name:
                    bone.playAction(self.creep_action,
                                     10,68,
                                     play_mode = bge.logic.KX_ACTION_MODE_PLAY,
                                     speed=1)
    
    def attack(self, enemy):
        if self["states"]=="attack":
            for bone in self.children:
                if bone.name == self.skeleton_name:
                    bone.playAction(self.creep_action,
                                              90,117.0000000000000000000000000000,
                                              play_mode = bge.logic.KX_ACTION_MODE_PLAY,
                                              speed=1)
                    print(bone.getActionFrame())
                    if math.fabs(bone.getActionFrame()-117 ) == 99e-2:
                        print("ss")
                        bone.stopAction()
                        self.sendMessage("attack",self.name,str(enemy))
                        self.sendMessage("attack_unitID",str(enemy.id),str(enemy)) 
                 
    def die_and_gold(self):
        if self.controller.sensors["Message"].positive:
            enemy = self.controller.sensors["Message"].bodies[0]
            self.sendMessage("reward","90",enemy)
            self.endObject()
            pass
