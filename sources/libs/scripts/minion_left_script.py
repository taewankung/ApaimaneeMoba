from bge import logic

from libs.apaimanee.characters.minion.minion import Minion

def move():
    cont =logic.getCurrentController()
    own = cont.owner

    animation = cont.actuators["animation"]

    minion = None
    if "team" in own:
        if own["team"] == "team2":
            minion = Minion(cont,
                            animation,
                            own,
                            "Armature_creep_left_team2",
                            "creep_left_action_team2"
                            )
        elif own["team"] == "team1":
            minion = Minion(cont,
                            animation,
                            own,
                            "Armature_creep_left_team1",
                            "creep_left_action_team1"
                            )
    if minion != None :
        
        #print("team: ", own["team"], " id: ", minion.id)
        minion.set_first_path("checkpoint_left1")
        minion.move_unit()
        minion.damaged()
        if own["hp"] <= 0:
            minion.die_and_gold()
