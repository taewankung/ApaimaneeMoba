from bge import logic
import time


cont = logic.getCurrentController()
scene_act = cont.actuators["Scene"]
cont.activate(scene_act)
print("ss")
