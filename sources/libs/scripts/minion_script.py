from bge import logic

from libs.apaimanee.characters.minion.minion import Minion



def initial(cont):

    owner = cont.owner
    skeleton_name = "Armature_creep_{}".format(owner['team'])
    creep_action = "creep_action_{}".format(owner['team'])
    multated_obj = Minion(owner,
                        skeleton_name=skeleton_name,
                        creep_action=creep_action)
    
def move():
    cont = logic.getCurrentController()
      
    if not type(cont.owner) is Minion:
        initial(cont)

    owner = cont.owner
#    print(owner.id) 
#    print(id(owner), owner['direction']) 
    owner.set_first_path("checkpoint1_{}_{}".format(owner["team"], owner['direction']))
       
    #if 'right' in own.name:
    owner.move_unit()
    owner.damaged()
    if owner["hp"] <= 0:
        owner.die_and_gold()
