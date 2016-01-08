from bge import logic


class GameUnit:
    def __init__(self,
                 #name, 
                 controller,
		         #max_hp, # maximum helth for game unit
                 #damaged=0,
                 #speed=0,
                 #attack_speed=0,
                 #armor = 1,
                 #act_message = 'None',
		         #sensor_message = 'None',
                 unit='',
                 enemy_list = []
                 ):
        self.cont = controller
        #self.sensor_message = sensor_message
        #self.act_message = act_message
        self.unit=unit
        self.enemy_list = enemy_list
#        self.own = self.cont.owner
#        self.name = name
#        self.max_hp = max_hp
#        self.current_hp = max_hp
#        self.damaged = damaged
#        self.speed = speed
#        self.attack_speed = attack_speed
#        self.armor = armor
#        self.alive = True
       
    def reduce_hp(self, damaged):
#        self.current_hp -= damaged*((100-armor)/100)
        self.unit["hp"] = damaged*((100-self.unit["armor"])/100)

    def regend_hp(self,hp):
        self.unit["hp"] += hp

    def die(self):
        self.unit["alive"] = False

    def get_alive(self):
        self.unit["alive"] = True
    #///////////////////// Interface ////////////////////////
    def move_unit(self):
        pass
    #//////////////////// Interface /////////////////////////
    def attack(self):
        pass
    
    def get_owner(self):
        return self.unit

    def show_status(self):
        print("Name: ", self.unit["name"])
        print("hp: ", self.unit["hp"])
        if(self.unit["alive"] == False ):
           print("alive status: Die")
        else:
           print("alive status: Alive")
