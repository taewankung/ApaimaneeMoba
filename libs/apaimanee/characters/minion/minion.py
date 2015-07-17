from bge import logic
from libs.apaimanee.characters.game_unit import GameUnit


class Minion(GameUnit):
    def __init__(self, name, max_hp,
                 damaged, speed, attack_speed
                 ,armor, minion_team,stop,
                 move, track, near, col_enemy,controller):
        super().__init__(name,
                        controller, 
                        max_hp,
                        damaged,
                        speed,
                        attack_speed,
                        armor)
        self.mininon_team = minion_team
        self.stop = stop;
        self.move = move;
        self.track = track;
        self.near = near;
        self.col_enemy = col_enemy;
    
    def get_gold(self, gold, hero):
        pass

    def move_unit(self):
        if self.near.positive:
            hitObjs = self.near.hitObjectList
            dist = 0
            obj = None
            for item in hitObjs:
                if item.getDistanceTo(self.own) < dist or dist ==0:
                    dist = item.getDistanceTo(self.own)
                    obj = item
            self.track.object = obj
            self.cont.activate(self.track)
            self.col_enemy.propName = "enemy"

            if self.col_enemy.positive :
                self.cont.deactivate(self.move)
            else:
                self.cont.activate(self.move)
        elif self.stop.positive:
            if self.own["id"]+1 < 4:
                self.stop.propName = "path" + str(self.own["id"]+1)
                self.own["mempath"]="path" + str(self.own["id"]+1)
                self.own["id"] += 1
            else : 
                self.cont.deactivate(self.move)
        else:
            self.cont.activate(self.move)
        self.cont.activate(self.track)
    
    def attack(self, enemy):
    	pass
   
    def get_gold(self):
    	pass
   
