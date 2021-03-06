from bge import logic
from bge import types
import bge
import math

from libs.apaimanee.characters.game_object import GameObject

#max_exp = [200, 300, 400, 500, 600, 700, 800, 900,
#           1000, 1100, 1200, 1300, 1400, 1500, 1600,
#           1700, 1800]

class Hero(GameObject):

    def __init__(self,
                 owner,
                 #click_point_obj,
                 bone_name='',
                 bone_action='',
                 ):
        super().__init__(owner)
        self.mouse = self.controller.sensors["Mouse"]
        self.track = self.controller.actuators["TrackTarget"]
        self.click = self.controller.sensors["ClickR"]
        self.move = self.controller.actuators["Move"]
        self.collision = self.controller.sensors["Collision"]
        self.enemy_col = self.controller.sensors["EnemyCol"]
        self.bone_name = bone_name
        self.bone_action = bone_action
        self.curren_scene = logic.getCurrentScene()
        #self.click_poin_obj = click_point_obj

    def getName(self):
        return self["unit_name"]

    def level_up(self,get_exp):
        self["exp"] += get_exp
        if self["exp"] >= self["max_exp"]:
            self["level"] += 1
            self["exp"] -= self["max_exp"]
            self["max_exp"] = max_exp[self.level-1]

    def regend_mana(self):
        pass

    def move_unit(self, target,start_frame,end_frame,move_speed):
        hitPosition = self.mouse.hitPosition
        hit_object = self.mouse.hitObject
        default_target = target

        if self.mouse.positive and "team" not in hit_object:
            if self.click.positive:
                self.track.object = default_target
                default_target.worldPosition.y = hitPosition.y
                default_target.worldPosition.x = hitPosition.x
                self.controller.activate(self.track)
                if self["states"]!='move':
                    self["states"] = "move"
                self.controller.activate(self.move)

        if self.collision.positive:
            if self["states"] == "move":
                self.controller.deactivate(self.move)
                self["states"] = "stand_by"
        elif not self.collision.positive:
            if self["states"] == "move":
                for bone in self.children:
                        if bone.name == str(self.name)+"_bone":
                            bone.playAction(str(bone.name)+"_action",
                                            start_frame,
                                            end_frame,
                                            play_mode = logic.KX_ACTION_MODE_PLAY,
                                            speed = 1)


    def attack(self, target,start_frame,end_frame,attack_speed):
        hitPosition = self.mouse.hitPosition
        hit_object = self.mouse.hitObject
        default_target = target
        click_enemy = False

        if self.click.positive and self.mouse.positive :
            click_enemy = True
            self.track.object = default_target
            default_target.worldPosition.y = hitPosition.y
            default_target.worldPosition.x = hitPosition.x
            self.controller.activate(self.track)
            if not type(hit_object) is bge.types.KX_GameObject:
                target["States"] =str(hit_object)
                target["IdObjClicked"] =hit_object.id

        if self.enemy_col.positive and self["states"] != "attack":
            self.controller.deactivate(self.move)
            self.children[self.bone_name].playAction(self.bone_action,
                                start_frame,
                                end_frame,
                                play_mode = logic.KX_ACTION_MODE_PLAY,
                                speed = attack_speed
                               )
            self["states"] = "attack"
        if math.fabs(self.children[self.bone_name].getActionFrame()-end_frame)< 99e-2:
            self.children[self.bone_name].stopAction()
            self["states"] = "end_attack"
            self.sendMessage('attack',str(self.name),target["States"])
            self.sendMessage('attack_unitID',target["IdObjClicked"],target["States"])

    def set_key(self, key):
        pass

    def gold_increase(self, gold):
        if self.controller.sensors["MessageReward"].positive:
            print(self.controller.sensors["MessageReward"].bodies)
            self["gold"] += int(self.controller.sensors["MessageReward"].bodies[0])

    def reborn(self):
        self["alive"] = True

    def die(self):
        self["alive"] = False

    def skill_action(self, start_frame, end_frame, sound_skill = None, obj_effect_name = None):
        have_sound = False
        if sound_skill :
            have_sound = True
        if obj_effect_name:
            effect_obj = self.current_scene.objectsInjected[obj_effect_name]
        self.children[self.bone_name].playAction(self.bone_action,
                                                start_frame,
                                                end_frame,
                                                play_mode = logic.KX_ACTION_MODE_PLAY,
                                                speed = 1
                                                )
        if math.fabs(self.children[self.bone_name].getActionFrame()-end_frame)< 99e-2:
            self.children[self.bone_name].stopAction()
            if have_sound :
                self.sound(sound_skill,"play")
                #   if have_sound:
                #        self.sound(sound_skill,"stop")

    def sound(self,sound_actuator_name,mode):
        sound = self.controller.actuators[sound_actuator_name]
        if mode == 'play' :
            self.controller.activate(sound)
        elif mode == 'stop':
            self.controller.deactivate(sound)

    def get_when_die(self, kda):
        gift=[]
        self["gold"] = kda * 500
        if gold > 500:
            gold = 500
        gift.append(self["gold"])
        self["exp"] = 500
        gift.append(self["exp"])
        return gift

    def show_status(self):
        print("level: ", self["level"])
        print("Status Hero")
        print("Name: ", self["name_unit"])
        print("hp: ", self["hp"])
        print("mana: ", self["mp"])
        print("gold: ", self["gold"])
        if(self["alive"] == False ):
            print("alive status: Die")
        else:
            print("alive status: Alive")
