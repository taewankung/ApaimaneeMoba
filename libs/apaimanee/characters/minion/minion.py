from bge import logic
from libs.apaimanee.characters.game_unit import GameUnit


class Minion(GameUnit):
    def __init__(self, name, max_hp,
                 damaged, speed, attack_speed
                 ,armor, minion_team,checkpoint
                 ,move, track, near, col_enemy,controller,command):
        super().__init__(name,
                        controller, 
                        max_hp,
                        damaged,
                        speed,
                        attack_speed,
                        armor)
        self.mininon_team = minion_team
        self.checkpoint = checkpoint
        self.move = move;
        self.track = track;
        self.near = near;
        self.col_enemy = col_enemy;
        self.command = command
        self.list_checkpoint = list(self.checkpoint.keys())
    
    def get_gold(self, gold, hero):
        pass

    def move_unit(self):
        scene = logic.getCurrentScene()
        self.own["mempath"] = self.list_checkpoint[int(self.own["go_to_next_checkpoint"])]
        self.track.object = scene.objects[self.own["mempath"]]
        if self.near.positive:
            hit_objs = self.near.hitObjectList
            dist = 0
            obj = None
            for item in hit_objs:
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
                self.cont.activate(self.command)
        elif self.checkpoint[str(self.own["mempath"])].positive:
            if len(self.list_checkpoint) > self.own["go_to_next_checkpoint"]+1:
                self.own["mempath"] = self.list_checkpoint[int(self.own["go_to_next_checkpoint"])]
                self.track.object = scene.objects[str(self.own["mempath"])]
                self.own["go_to_next_checkpoint"]+=1
                print(self.track.object)
                print(self.own["go_to_next_checkpoint"])
            else:
                self.cont.deactivate(self.move)
        else:
            self.cont.activate(self.move)
            self.cont.activate(self.command)
        self.cont.activate(self.track)
    
    def attack(self, enemy):
    	pass
   
    def get_gold(self):
    	pass
   
