from bge import logic
import sys

from libs.apaimanee.characters.game_unit import GameUnit

max_exp = [200, 300, 400, 500, 600, 700, 800, 900,
           1000, 1100, 1200, 1300, 1400, 1500, 1600,
           1700, 1800] 


class Hero(GameUnit):

    def __init__(self, name, max_hp,armor, max_mana,
                 damaged, hero_team,speed, 
                 sensor_mouse, sensor_click,
                 sensor_collition, act_track, act_move,
                 controller,
                 attack_speed=0.5) :
       
        super().__init__(name,
                         controller, 
                         max_hp, 
                         damaged,
                         speed,
                         attack_speed,
                         armor)

        self.mouse = sensor_mouse
        self.track = act_track
        self.click = sensor_click
        self.collition = sensor_collition
        self.move = act_move
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
            target.worldPosition.y = hitPosition.y
            target.worldPosition.x = hitPosition.x
            self.cont.activate(self.track)
            self.cont.activate(self.move)
        if self.collition.positive:
            self.cont.deactivate(self.move)
        pass

    def attack(self, enemy):
        pass

    def skill_action(self, skill):
        pass

    def cooldown_skill(self,skill):
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
