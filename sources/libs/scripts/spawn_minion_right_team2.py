from bge import logic
from libs.apaimanee.characters.SpawnUnit import SpawnUnit
def run():
    scene = logic.getCurrentScene()
    #unit = scene.objects["Armature_creep"]
    cont = logic.getCurrentController()
    spawner = cont.owner
    obj = scene.objectsInactive["box_creep_right_team2"]
    spawn_unit = SpawnUnit(spawner,obj)
    spawn_unit.spawn(10)
