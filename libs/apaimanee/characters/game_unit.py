from bge import logic


class GameUnit:
    def __init__(self,
                 name, 
                 controller,
		         max_hp, # maximum helth for game unit
                 damaged=0,
                 speed=0,
                 attack_speed=0,
                 armor = 1,
                 act_message = 'None',
		         sensor_message = 'None',
                 objects='',
                 enemy_list = []
                 ):
        self.cont = controller
        self.own = self.cont.owner
        self.name = name
        self.sensor_message = sensor_message
        self.act_message = act_message
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.damaged = damaged
        self.speed = speed
        self.attack_speed = attack_speed
        self.armor = armor
        self.alive = True
        self.objects=objects
        self.enemy_list = enemy_list
        
    def reduce_hp(self, damaged):
        self.current_hp -= damaged*((100-armor)/100)
        self.objects["hp"] = damaged*((100-armor)/100)

    def regend_hp(self,hp):
        self.current_hp += hp

    def die(self):
        self.alive = False

    def get_alive(self):
         return alive
    #///////////////////// Interface ////////////////////////
    def move_unit(self):
        pass
    #//////////////////// Interface /////////////////////////
    def attack(self):
        pass
    
    def get_owner(self):
        return self.own

    def show_status(self):
        print("Name: ", self.name)
        print("hp: ", self.current_hp)
        if(self.alive == False ):
           print("alive status: Die")
        else:
           print("alive status: Alive")
