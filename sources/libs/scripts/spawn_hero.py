import bge
from libs.apaimanee.characters.spawn_unit import SpawnUnit

def spawn():
    controller = bge.getCurrentController()
    owner = controller.owner
    spawn = controller.actuators["Spawn"]
    sensors = controller.sensors
    spawn.object = sensors["Message"].body
    controller.activate(spawn)
