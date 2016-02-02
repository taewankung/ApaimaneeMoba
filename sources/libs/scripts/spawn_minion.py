from bge import logic
from libs.apaimanee.characters.SpawnUnit import SpawnUnit

def run():
    scene = logic.getCurrentScene()
    #unit = scene.objects["Armature_creep"]
    cont = logic.getCurrentController()
    spawner = cont.owner
    obj = scene.objectsInactive["box_minion"]
    #obj['mempath'] = 'chekpoint_central1'
    spawn_unit = SpawnUnit(spawner, obj)

    spawn_unit.spawn(30)

    minions = spawn_unit.last_spawn_object()
    for minion in minions:
        if minion:
            minion["team"] = spawner['team']
            minion["direction"] =spawner['direction']
