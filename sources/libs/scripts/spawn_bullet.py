from bge import logic
from libs.apaimanee.characters.building.spawn_bullet import SpawnBullet
from libs.apaimanee.characters.building.tower import Tower

from bge import logic

def initial(cont):
    owner = cont.owner
    multated_obj = SpawnBullet(owner, bullet="bullet", time=2)
    
def spawn_bullet():
    cont =logic.getCurrentController()
    if not type(cont.owner) is SpawnBullet:
        initial(cont)
    owner = cont.owner
    scene = logic.getCurrentScene()

    tower_obj = scene.objects[owner["tower"]]
    #print(id(tower_obj))

    owner.track(tower_obj.attack())
    owner.spawn(tower_obj.attack())
