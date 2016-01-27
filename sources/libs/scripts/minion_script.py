from bge import logic

from libs.apaimanee.characters.minion.minion import MinionController



def initial(cont):

    owner = cont.owner
    skeleton_name = "Armature_creep_{}_{}".format(owner['direction'], owner['team'])
    creep_action = "creep_{}_action_{}".format(owner['direction'], owner['team'])
    controller = MinionController(skeleton_name=skeleton_name, creep_action=creep_action)
    cont.owner['controller'] = controller
    
def move():
    cont = logic.getCurrentController()
    owner = cont.owner
      
    if not 'controller' in owner:
        initial(cont)

    minnion_ctl = cont.owner['controller']
   
    print(minnion_ctl.id) 
    if 'left_team' in owner.name:
        minnion_ctl.set_first_path("checkpoint_left1")
    if 'mid' in owner.name:
        minnion_ctl.set_first_path("checkpoint_central1")
    #if 'right' in own.name:
    minnion_ctl.move_unit()
    minnion_ctl.damaged()
    if owner["hp"] <= 0:
        minnion_ctl.die_and_gold()
