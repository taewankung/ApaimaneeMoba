import bge

def spawn(hero = "sinsamut"):
    controller = bge.getCurrentController()
    owner = controller.owner
    spawn = controller.actuators["Spawn"]
    controller.activate(spawn)
