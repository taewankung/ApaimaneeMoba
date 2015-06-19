from bge import logic
from ApaimaneeMoba.lib.characters.game_unit import GameUnit


class Minion(GameUnit):
    def __init__(self, name, max_hp,
                 damaged, speed, attack_speed
                 armor,minion_team):
        super().__init__(self, name, max_hp,damaged, speed, attack_speed, armor)
        self.mininon_team = minion_team
    
    def get_gold(self, gold, hero):
        pass

    def move_unit(self):
        pass

    def attack(self, enemy):
    	pass
   
    def get_gold(self):
    	pass
   