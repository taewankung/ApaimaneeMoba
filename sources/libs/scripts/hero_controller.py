from bge import logic
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
    target = scene.objects["Target"]
    #animation = scene.objects["metarig"]
    #hero_object= scene.objects["box_hero"]

    track_target = cont.actuators["TrackTarget"]
    #enemy_list=["box_creep_left_team2",
     #           "box_creep_right_team2",
      #          "box_creep_mid_team2",
      #          "thai_tower_mid_front",
      #          "thai_tower_mid_mid",
      #          "thai_tower_mid_back",
      #          "thai_tower_home_left",
      #          "thai_tower_home_right",
      #          "thai_tower_right_front",
      #          "thai_tower_right_mid",
      
      #          "thai_tower_right_back",
      #          "thai_tower_left_front",
      #          "thai_tower_left_mid",
      #          "thai_tower_left_back"
      #          ]
    hero_dict = {
                    "sinsamut":{"move_start":156,
                                "move_end":174,
                                "attack_start":10,
                                "attack_end":37

                    }
                }
    owner.move_unit(target,hero_dict[owner.name]["move_start"],
                    hero_dict[owner.name]["move_end"],1
                    )
    owner.attack(target,hero_dict[owner.name]["attack_start"],
                 hero_dict[owner.name]["attack_end"],1
                 )
    owner.gold_increase(1)
    owner.damaged()
#hero.show_status()
