from bge import logic
from bge import events
from libs.apaimanee.characters.hero.hero import Hero

def initial(cont):
    owner = cont.owner
    mutage_obj = Hero(owner,bone_name=str(owner.name)+"_bone",bone_action=str(owner.name)+"_bone_action")

def hero_controller():
    cont = logic.getCurrentController()
    scene = logic.getCurrentScene()
    if not type(cont.owner) is Hero:
        initial(cont)
    owner = cont.owner
    target = scene.objects["target_player1"]
    #animation = scene.objects["metarig"]
    #hero_object= scene.objects["box_hero"]

    track_target = cont.actuators["TrackTarget"]
    hero_dict = {
                    "sinsamut":{"move_start":156,
                                "move_end":174,
                                "attack_start":70,
                                "attack_end":90,
                                "skill_1_start":10,
                                "skill_1_end":37
                    },
                    "apaimanee":{"move_start":0,
                                 "move_end":30,
                                 "attack_start":60,
                                 "attack_end":64,
                                 "skill_1_start":60,
                                 "skill_1_end":64
,
                    }
                }
    owner.move_unit(target,hero_dict[owner.name]["move_start"],
                    hero_dict[owner.name]["move_end"],1
                    )
    owner.attack(target,hero_dict[owner.name]["attack_start"],
                 hero_dict[owner.name]["attack_end"],1
                 )
    for key,status in cont.sensors["Keyboard"].events:
        if  status == logic.KX_INPUT_JUST_ACTIVATED:
                if key == events.QKEY:
                    owner.skill_action(hero_dict[owner.name]["skill_1_start"],
                                      hero_dict[owner.name]["skill_1_end"],
                                      "SoundSkill1"
                                     )
                    print("skill1")
                elif key == events.WKEY:
                    print("skill2")
                elif key == events.EKEY:
                    print("skill3")
    owner.gold_increase(1)
    owner.damaged()
#hero.show_status()
