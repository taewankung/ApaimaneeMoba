from bge import logic
from bge import types
import bpy 
 
import sys
import time

from libs.apaimanee.characters.game_unit import GameUnit

max_exp = [200, 300, 400, 500, 600, 700, 800, 900,
           1000, 1100, 1200, 1300, 1400, 1500, 1600,
           1700, 1800] 

class Hero(GameUnit):
    
    def __init__(self, name, max_hp,armor, max_mana,
                 damaged, hero_team,speed,
                 controller,
                 attack_speed=0.5,
                 act_message='None',
                 sensor_message='None',animation='',objects=''):
            #self.delay += self.attack_speed; 
       
        super().__init__(name,
                         controller, 
                         max_hp, 
                         damaged,
                         speed,
                         attack_speed,
                         armor,
                         act_message,
                         sensor_message,objects)
        self.mouse = self.cont.sensors["Mouse"]
        self.track = self.cont.actuators["TrackTarget"]
        self.click = self.cont.sensors["ClickR"]
        self.move = self.cont.actuators["Move"]
        self.collition = self.cont.sensors["Collision"]
        self.mana = max_mana
        self.max_mana = max_mana
        self.hero_team = hero_team
        self.level = 1
        self.gold = 650
        self.kill = 0
        self.die = 0
        self.assist = 0
        self.kda = self.kill+self.assist/((self.die+1))
        self.exp = 0
        self.max_exp = max_exp[self.level-1]
        self.animation = animation
        self.state = self.own["states"]

    def level_up(self,get_exp):
        self.exp += get_exp
        if self.exp >= exp:
            self.level += 1
            self.exp -= self.max_exp
            self.max_exp = [self.level-1]

    def regend_mana(self):
        pass
    
    def move_unit(self, target):
        self.track.object = target
        hitPosition = self.mouse.hitPosition
        if self.click.positive:
           # self.own.sendMessage("move","","metarig")
            target.worldPosition.y = hitPosition.y
            target.worldPosition.x = hitPosition.x
            self.cont.activate(self.track)
            self.cont.activate(self.move)
            if self.state=='stand_by':
                self.objects["states"] = "move"
        if self.collition.positive:
            self.cont.deactivate(self.move)
            self.objects["states"] = "stand_by"
        elif self.state=='move':
            self.own.sendMessage("move","",str(self.animation))
           # print("move")
            #self.state="stand_by"

    def attack(self, target):
        hitObject = self.mouse.hitObject
        if str(hitObject == "tower") and self.click.positive :
            target["states"]=str(hitObject)
        if self.cont.sensors["team2"].positive and target["states"] == "tower":
            self.own.sendMessage('attack',"",str(self.animation))
            #self.own.sendMessage('attack',"",target["states"])
            self.objects["states"]='attack'
            if self.objects.sensors["Message"].positive:
                self.own.sendMessage('attack','',target["states"])
            #print(self.objects["test"])
        if not self.cont.sensors["team2"].positive:
            self.objects["states"]='move'
            self.objects["test"]=0;

    def skill_action(self, skill):
        pass

    def cooldown_skill(self, skill):
        pass

    def set_key(self, key):
        pass

    def gold_increase(self, gold):
        self.gold += gold

    def reborn(self):
        self.alive = True

    def die(self):
        self.alive = False

    def get_when_die(self, kda):
        gift=[]
        gold = kda * 500
        if gold > 500:
            gold = 500
        gift.append(gold)
        exp = 500
        gift.append(exp)
        return gift

    def show_status(self):
        print("level: ", self.level)
        print("Status Hero")
        print("Name: ", self.name)
        print("hp: ", self.current_hp)
        print("mana: ", self.mana)
        print("gold: ", self.gold)
        if(self.alive == False ):
            print("alive status: Die")
        else:
            print("alive status: Alive")
