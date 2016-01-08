from bge import logic
from libs.apaimanee.characters.game_unit import GameUnit


class Minion(GameUnit):
    def __init__(self, 
                 #name, max_hp,
                 #damaged, speed, attack_speed,
                 #armor, minion_team,
                 checkpoint,
                 #move, track, near, col_enemy,
                 controller,animation,
                 unit,
                 #act_message='None',
                 #sensor_message='None',
                 enemy_list=[]):
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
                        enemy_list
                        )
        #self.mininon_team = minion_team
        self.checkpoint = checkpoint
        #self.act_message = act_message
        #self.sensor_message = sensor_message
        self.move = self.cont.actuators["move"]
        self.track = self.cont.actuators["track"]
        self.near = self.cont.sensors["near_enemy"]
        self.col_enemy = self.cont.sensors["col_enemy"]
        self.animation = self.cont.actuators["animation"]
        self.list_checkpoint = list(self.checkpoint.keys())
    
    def get_gold(self, gold, hero):
        pass

    def move_unit(self):
        scene = logic.getCurrentScene()
        self.unit["mempath"] = self.list_checkpoint[int(self.unit["go_to_next_checkpoint"])]
        self.track.object = scene.objects[self.unit["mempath"]]
        if self.near.positive:
            hit_objs = self.near.hitObjectList
            dist = 0
            obj = None
            for item in hit_objs:
                if item.getDistanceTo(self.unit) < dist or dist ==0:
                    dist = item.getDistanceTo(self.own)
                    obj = item
            self.track.object = obj
            self.cont.activate(self.track)
            self.col_enemy.propName = "enemy"
            if self.col_enemy.positive :
                self.cont.deactivate(self.move)
            else:
                self.cont.activate(self.move)
                self.cont.activate(self.animation)
        elif self.checkpoint[str(self.unit["mempath"])].positive:
            if len(self.list_checkpoint) > self.unit["go_to_next_checkpoint"]+1:
                self.own["mempath"] = self.list_checkpoint[int(self.unit["go_to_next_checkpoint"])]
                self.track.object = scene.objects[str(self.own["mempath"])]
                self.unit["go_to_next_checkpoint"]+=1
                print(self.track.object)
                print(self.unit["go_to_next_checkpoint"])
            else:
                self.cont.deactivate(self.move)
        else:
            self.cont.activate(self.move)
            self.cont.activate(self.animation)
        self.cont.activate(self.track)
    
    def attack(self, enemy):
    	pass
   
    def get_gold(self):
    	pass
   
