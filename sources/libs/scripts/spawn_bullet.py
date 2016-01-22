from bge import logic
from libs.apaimanee.characters.building.SpawnBullet import SpawnBullet
from libs.apaimanee.characters.building.tower import Tower

from bge import logic


def spawn_bullet():
    cont =logic.getCurrentController()
    scene = logic.getCurrentScene()
    own = cont.owner
    own_object = scene.objects[str(own)]
    enemy_list = []
    if own["tower"] in scene.objects: 
        tower_obj = scene.objects[str(str(own["tower"]))]
        tower_cont = tower_obj.controllers['Python']
        tower = Tower(tower_cont,tower_obj,own,enemy_list)
        if own.name in scene.objects:
            #print(own.name)
            unit_spawn = scene.objects[own.name]
            bullet = "bullet"
            spawn_bullet = SpawnBullet(unit_spawn,cont,bullet,2.0)
            spawn_bullet.track(tower.attack())
            spawn_bullet.check_destroy()
