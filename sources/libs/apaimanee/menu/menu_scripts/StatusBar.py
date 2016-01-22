from bge import logic
class StatusBar:
    #message_dict = Message_sensor
    #obj_bar = KX_GameObject in bge.logic Example: hp_bar,mp_bar and etc.
    #name_act = animetion name of object
    #max_value_name = name of max valiable in KX_GameObject
    #current_value_name = name of current valiable in KX_GameObject
    #ghost_value_name = name of ghost valiable in KX_GameObject
    #unit = KX_GameObject link status with status bar 
    def __init__(self,name_act,obj_bar,
                max_value_name,
                current_value_name,
                ghost_value_name,
                unit
                ):
            self.obj_bar =obj_bar
            self.value={"max_value":max_value_name,
                        "value":current_value_name,
                        "ghost_value":ghost_value_name
                       }
            self.name_act = name_act
            self.unit = unit
    
    def reduce(self,damage):
        value = self.value["value"]
        ghost_value = self.value["ghost_value"]
        max_value = self.value["max_value"]
        if(self.unit[value]>0): 
        # status_bar change value
            self.current_per_value = self.unit[ value ]/self.unit[max_value]*100
            self.ghost_per_value = self.unit[ghost_value]/self.unit[max_value]*100
            self.anime_start = self.ghost_per_value*10
            self.anime_end = self.current_per_value*10
            self.obj_bar.playAction(self.name_act,
                           self.anime_start,
                           self.anime_end,
                           play_mode = logic.KX_ACTION_MODE_PLAY,
                           speed=100.0)
    
    def increase(self,inc_value):
        value = self.value["value"]
        ghost_value = self.value["ghost_value"]
        max_value = self.value["max_value"]
        if(self.unit[value]<=self.unit[max_value]):
        # status_bar change value
            self.current_per_value = self.unit[ value ]/self.unit[max_value]*100
            self.ghost_per_value = self.unit[ghost_value]/self.unit[max_value]*100
            self.anime_end = self.current_per_value*10
            self.anime_start = self.ghost_per_value*10
            self.obj_bar.playAction(self.name_act,
                           self.anime_start,
                           self.anime_end,
                           play_mode = logic.KX_ACTION_MODE_PLAY,
                           speed=100.0)
    def update(self):
        if self.unit[self.value["value"]] < self.unit[self.value['ghost_value']]:
            self.reduce(self.unit[self.value['ghost_value']]-self.unit[self.value["value"]] )
            self.unit[self.value['ghost_value']]=self.unit[self.value["value"]]  
        if self.unit[self.value["value"]] > self.unit[self.value['ghost_value']]:
            print("ss")
            self.unit[self.value['ghost_value']]=self.unit[self.value["value"]]  
            self.increase(self.unit[self.value["value"]]-self.unit[self.value['ghost_value']])
           # pass  
