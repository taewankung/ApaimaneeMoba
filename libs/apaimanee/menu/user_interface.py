from bge import logic
from ApaimaneeMoba.lib.characters.hero import Hero

class User_interface:
    def __init__(self,hero):
        self.current_hp = hero.current_hp
        self.max_hp = hero.max_hp
        self.mana = hero.mana
        self.max_mana = hero.max_mana
        self,damaged = hero.damaged
        self.speed = hero.speed
        self.attack_speed = attack_speed
        self.armor = hero.armor
        self.gold = hero.gold
        self.level = hero.level
        self.kill = hero.kill
        self.die = hero.die
        self.assist = hero.assist
        self.exp = hero.exp
        self.max_exp = hero.max_exp

    def get_item(item):
        pass
