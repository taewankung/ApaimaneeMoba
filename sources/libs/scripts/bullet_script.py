from libs.apaimanee.characters.building.bullet import Bullet
from bge import logic
from libs.apaimanee.characters.building.tower import Tower



def bullet_script_run() :
    scene = logic.getCurrentScene()
    cont = logic.getCurrentController()
    unit = cont.owner
    bullet = Bullet(unit)
    #message = cont.sensors["Message"]
    #print(str(cont.sensors["Message"].bodies[0]))
    bullet.attack(200)
