from bge import logic
from libs.apaimanee.characters.building.tower import Tower
from libs.apaimanee.characters.building.SpawnBullet import SpawnBullet
from libs.apaimanee.characters.hero.hero import Hero




def tower_controller(unit, spawner,scene,enemy_list ):
        if unit in scene.objects:
            if spawner in scene.objects:
                unit_spawn_bullet = scene.objects[spawner]
                spawn_bullet = SpawnBullet(unit_spawn_bullet,
                                           unit_spawn_bullet.controllers["Python"],
                                           "bullet",
                                           2)
                tower_unit = scene.objects[unit]
                cont_tower = tower_unit.controllers["Python"]
                tower = Tower(cont_tower,tower_unit,unit_spawn_bullet,enemy_list)
                tower.damaged()
                tower.attack()
                if tower_unit["hp"] == 0:
                    tower.destroyed()


def tower_controller_run():
    spawn_bullets = {
                 "tower_mid_front":"spawn_bullet_mid_front",
                 "tower_mid_mid":"spawn_bullet_mid_mid",
                 "tower_mid_back":"spawn_bullet_mid_back",
                 "tower_left_front":"spawn_bullet_left_front",
                 "tower_left_mid":"spawn_bullet_left_mid",
                 "tower_left_back":"spawn_bullet_left_back",
                 "tower_right_front":"spawn_tower_right_front",
                 "tower_right_mid":"spawn_tower_right_mid",
                 "tower_right_back":"spawn_tower_right_back",
                 "tower_home_left":"spawn_bullet_home_left",
                 "tower_home_right":"spawn_bullet_home_right",
                 "thai_tower_mid_front":"thai_spawn_bullet_mid_front",
                 "thai_tower_mid_mid":"thai_spawn_bullet_mid_mid",
                 "thai_tower_mid_back":"thai_spawn_bullet_mid_back",
                 "thai_tower_left_front":"thai_spawn_bullet_left_front",
                 "thai_tower_left_mid":"thai_spawn_bullet_left_mid",
                 "thai_tower_left_back":"thai_spawn_bullet_left_back",
                 "thai_tower_right_front":"thai_spawn_bullet_right_front",
                 "thai_tower_right_mid":"thai_spawn_bullet_right_mid",
                 "thai_tower_right_back":"thai_spawn_bullet_right_back",
                 "thai_tower_home_left":"thai_spawn_bullet_home_left",
                 "thai_tower_home_right":"thai_spawn_bullet_home_right",
                }
    scene = logic.getCurrentScene()
    cont = logic.getCurrentController()
    enemy_list = ['']

    for tower_position in spawn_bullets.keys():
        tower_controller(tower_position, spawn_bullets[tower_position],scene,enemy_list )

#if "tower_mid_mid" in scene.objects:
#    if "spawn_bullet_mid_mid" in scene.objects:
#        spawn_bullet = scene.objects["spawn_bullet_mid_mid"]
#        tower_unit = scene.objects["tower_mid_mid"]
#        cont_tower = tower_unit.controllers["Python"]    
#        tower = Tower(cont_tower,tower_unit,spawn_bullet,enermy_list)
#        tower.damaged()
#        tower.attack(10)
#        if tower_unit["hp"] == 0:
#            tower.destroyed()            
