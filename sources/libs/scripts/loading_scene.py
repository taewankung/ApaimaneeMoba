from bge import logic
import time

import sys

def loading_scene():
    cont = logic.getCurrentController()
    scene_act = cont.actuators["Scene"]
    cont.activate(scene_act)
    print("arg:", sys.argv)
