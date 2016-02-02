from bge import logic
from libs.apaimanee.characters.building.tower import Tower
#from libs.apaimanee.characters.building.SpawnBullet import SpawnBullet
def initial(cont):
    owner = cont.owner
    spawn_str = "spawn_bullet"+owner.name[5:]
    #print(spawn_str)
    multated_obj = Tower(owner,spawn_bullet=spawn_str)

def run():
    #tower_unit = scene.objects[unit]
    #cont_tower = tower_unit.controllers["Python"]
    cont = logic.getCurrentController()
    if not type(cont.owner) is Tower:
        initial(cont)
    owner = cont.owner
    #print("tower ",owner.id)
    owner.damaged()
    owner.attack()
    if owner["hp"] == 0:
        owner.destroyed()
