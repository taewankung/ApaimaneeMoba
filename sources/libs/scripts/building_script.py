from bge import logic
from libs.apaimanee.characters.building.building import Building
def initial(cont):
    owner =cont.owner
    multated_obj = Building(owner)

def run():
    cont = logic.getCurrentController()
    if not type(cont.owner) is Building:
        initial(cont)
    owner = cont.owner
    owner.damaged()
    if owner["hp"] <= 0:
        owner.destroyed()

