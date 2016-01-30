from bge import logic
from bge import render
from .StatusBar import StatusBar

class HudCamera :
    def __init__(self,
                contoller,
                obj_camera,
                unit=None,
                hud_dict='',
                speed =0.01,
                ):
                self.cont = contoller
                self.mouse = self.cont.sensors["mouse"]
                self.obj_camera = obj_camera
                self.hud_dict = hud_dict
                self.speed = speed
                self.unit = unit
     
    def unit_status(self):
        if self.unit != None:
            if "name_unit" in self.unit:
                self.hud_dict["text_name_hero"].text = self.unit["name_unit"]            
            if "hp" in self.unit and "max_hp" in self.unit:
                self.hud_dict["text_hp_bar"].text = str(self.unit['hp'])+'/'+str(self.unit["max_hp"])
            else: 
                self.hud_dict["text_hp_bar"].text = str(0)+'/'+str(0)
            if "name_unit" in self.unit and "max_mp":
                self.hud_dict["text_mp_bar"].text = str(self.unit['mp'])+'/'+str(self.unit["max_mp"])
            else: 
                self.hud_dict["text_mp_bar"].text = str(0)+'/'+str(0)
            if "dmg" in self.unit:
                self.hud_dict["text_dmg"].text = 'Dmg: '+str(self.unit['dmg'])
            else: 
                self.hud_dict["text_dmg"].text = str(0)
            if "magic" in self.unit:
                self.hud_dict["text_magic"].text = 'Mag: '+str(self.unit['magic'])
            else:
                self.hud_dict["text_magic"].text = str(0)
            if "armor" in self.unit:
                self.hud_dict["text_armor"].text = 'Arm: '+str(self.unit['armor'])
            else: 
                self.hud_dict["text_armor"].text = str(0)
            if "gold" in self.unit:
                self.hud_dict["text_gold"].text = 'Gold: '+str(self.unit['gold'])
            else: 
                self.hud_dict["text_gold"].text = str(0)
        if "hp_bar" in self.hud_dict:
            hp_bar = StatusBar("hp_bar_action",
                                self.hud_dict["hp_bar"],
                                "max_hp","hp","ghost_hp",
                                self.unit
                                )
        if "mp_bar" in self.hud_dict:
            mp_bar = StatusBar("mp_bar_action",
                                self.hud_dict["mp_bar"],
                                "max_mp","mp","ghost_mp",
                                self.unit
                               )
            mp_bar.update()
            hp_bar.update()
        
    def move(self):
        scene = logic.getCurrentScene()
        if self.mouse.position[0] >= render.getWindowWidth()-15: #move Right
            self.obj_camera.worldPosition.x = self.obj_camera.worldPosition.x+self.speed
            for obj in self.hud_dict.keys() :
                self.hud_dict[obj].worldPosition.x = self.hud_dict[obj].worldPosition.x+self.speed

        if self.mouse.position[0] <= 15: #move Left
            self.obj_camera.worldPosition.x = self.obj_camera.worldPosition.x-self.speed
            for obj in self.hud_dict.keys() :
                self.hud_dict[obj].worldPosition.x = self.hud_dict[obj].worldPosition.x-self.speed

        if self.mouse.position[1] >= render.getWindowHeight()-15: #move Down
            self.obj_camera.worldPosition.y = self.obj_camera.worldPosition.y-self.speed 
            for obj in self.hud_dict.keys() :
                self.hud_dict[obj].worldPosition.y = self.hud_dict[obj].worldPosition.y-self.speed

        if self.mouse.position[1] <= 15: #move UP
            self.obj_camera.worldPosition.y = self.obj_camera.worldPosition.y+self.speed
            for obj in self.hud_dict.keys() :
                self.hud_dict[obj].worldPosition.y = self.hud_dict[obj].worldPosition.y+self.speed
