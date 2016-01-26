from bge import logic
from libs.apaimanee.characters.hero.hero import Hero
def hero_controller():
    controller = logic.getCurrentController()
    scene = logic.getCurrentScene()
    target = scene.objects["Target"]
    animation = scene.objects["metarig"]
    hero_object= scene.objects["box_hero"]

    track_target = controller.actuators["TrackTarget"]
    enemy_list=["box_creep_left_team2",
                "box_creep_right_team2",
                "box_creep_mid_team2",
                "thai_tower_mid_front",
                "thai_tower_mid_mid",
                "thai_tower_mid_back",
                "thai_tower_home_left",
                "thai_tower_home_right",
                "thai_tower_right_front",
                "thai_tower_right_mid",
                "thai_tower_right_back",
                "thai_tower_left_front",
                "thai_tower_left_mid",
                "thai_tower_left_back"
                ]
    hero = Hero(controller,"metarig","metarigAction.002",hero_object,enemy_list)
    hero.move_unit(target,30,50,1)
    hero.attack(target,180,195,1)
    hero.gold_increase(1)
    hero.damaged()
#hero.show_status()
