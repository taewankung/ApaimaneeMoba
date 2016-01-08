from bge import logic
from bge import types

import sys
import time

from libs.apaimanee.characters.game_unit import GameUnit

max_exp = [200, 300, 400, 500, 600, 700, 800, 900,
           1000, 1100, 1200, 1300, 1400, 1500, 1600,
           1700, 1800] 

class Hero(GameUnit):
    
    def __init__(self,# name, max_hp,armor, max_mana,
                 #damaged, 
                 #hero_team,#speed,
                 controller,
                 #attack_speed=0.5,
                 #act_message='None',
                 #sensor_message='None',
                 animation='',
                 unit='',
                 enemy_list=[]):
            #self.delay += self.attack_speed; 
       
        super().__init__(#name,
                         controller, 
                         #max_hp, 
                         #damaged,
                         #speed,
                         #attack_speed,
                         #armor,
                         #act_message,
                         #sensor_message,
                         unit,
                         enemy_list)
        
        self.mouse = self.cont.sensors["Mouse"]
        self.track = self.cont.actuators["TrackTarget"]
        self.click = self.cont.sensors["ClickR"]
        self.move = self.cont.actuators["Move"]
        self.collition = self.cont.sensors["Collision"]
        self.animation = animation
    
    def getName(self):
        return self.name

    def level_up(self,get_exp):
        self.unit["exp"] += get_exp
        if self.unit["exp"] >= self.unit["max_exp"]:
            self.unit["level"] += 1
            self.unit["exp"] -= self.unit["max_exp"]
            self.unit["max_exp"] = max_exp[self.level-1]

    def regend_mana(self):
        pass
    
    def move_unit(self, target):
        scene = logic.getCurrentScene()
        hitPosition = self.mouse.hitPosition
        hit_object = self.mouse.hitObject
        default_target = scene.objects["Target"]
        #print("in hero.py line 65:"+str(self.mouse.hitObject))
        if self.click.positive and (self.enemy_list.count(str(hit_object)) == 0):
            self.track.object = default_target
            default_target.worldPosition.y = hitPosition.y
            default_target.worldPosition.x = hitPosition.x
            self.cont.activate(self.track)
            self.cont.activate(self.move)
            if self.unit["states"]=='stand_by':
                self.unit["states"] = "move"
        elif self.click.positive and (self.enemy_list.count(str(hit_object))  > 0):
            self.track.object = hit_object
            self.cont.activate(self.track)
            self.cont.activate(self.move)
        if self.collition.positive:
            self.cont.deactivate(self.move)
            self.unit["states"] = "stand_by"
        elif self.unit["states"]=='move':
            self.unit.sendMessage("move","",str(self.animation))

    def attack(self, target):
        hitObject = self.mouse.hitObject
        #print(enemy_list.count(str(hitObject)))
        if self.enemy_list.count(str(hitObject)) > 0 and self.click.positive :
            target["states"]=str(hitObject)
        if self.cont.sensors["team2"].positive and self.enemy_list.count(target["states"])>0:
            #print(self.enemy_list)
            self.unit.sendMessage('attack',"",str(self.animation))
            #self.unit.sendMessage('attack',"",target["states"])
            self.unit["states"]='attack'
            if self.unit.sensors["Message"].positive:
                self.unit.sendMessage('attack',str(self.unit.name),target["states"])
        if not self.cont.sensors["team2"].positive:
            self.unit["states"]='move'
            #self.unit["test"]=0;

    def skill_action(self, skill):
        pass

    def cooldown_skill(self, skill):
        pass

    def set_key(self, key):
        pass

    def gold_increase(self, gold):
        if self.cont.sensors["Message_reward"].positive:
            print(self.cont.sensors["Message_reward"].bodies)
            self.unit["gold"] += int(self.cont.sensors["Message_reward"].bodies[0])

    def reborn(self):
        self.unit["alive"] = True

    def die(self):
        self.unit["alive"] = False

    def get_when_die(self, kda):
        gift=[]
        self.unit["gold"] = kda * 500
        if gold > 500:
            gold = 500
        gift.append(self.unit["gold"])
        self.unit["exp"] = 500
        gift.append(self.unit["exp"])
        return gift

    def show_status(self):
        print("level: ", self.unit["level"])
        print("Status Hero")
        print("Name: ", self.unit["name_unit"])
        print("hp: ", self.unit["hp"])
        print("mana: ", self.unit["mp"])
        print("gold: ", self.unit["gold"])
        if(self.unit["alive"] == False ):
            print("alive status: Die")
        else:
            print("alive status: Alive")
