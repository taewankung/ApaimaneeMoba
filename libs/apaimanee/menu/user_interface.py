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

    def show_item(self):
        pass

    def show_hp(self):
        pass

    def show_maxhp(self):
        pass

    def show_mana(self):
        pass

    def show_maxmana(self):
        pass

    def show_reborn(self):
        pass

    def show_cooldown(self):
        pass

    def show_kill(self):
        pass

    def show_die(self):
        pass

    def show_assist(self):
        pass

    def show_score(self):
        pass

    def show_minimap(self):
        pass

    def show_damage(self):
        pass

    def show_armor(self):
        pass

    def show_speed(self):
        pass

    def show_attackspeed(self):
        pass

    def show_name(self):
        pass