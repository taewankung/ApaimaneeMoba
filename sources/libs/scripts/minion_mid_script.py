from bge import logic

from libs.apaimanee.characters.minion.minion import Minion

def move():
    cont =logic.getCurrentController()
    own = cont.owner

    animation = cont.actuators["animation"]

    minion = None
    if "team2" in own:
        minion = Minion(
                        cont,
                        animation,
                        own,
                        own["team2"],
                        "Armature_creep_mid_team2",
                        "creep_mid_action_team2"
                        )
    else:
        minion = Minion(cont,
                        animation,
                        own,
                        own["team1"],
                        "Armature_creep_mid_team1",
                        "creep_action_mid_team1"
                        )
    if minion != None :
        minion.set_first_path("checkpoint_central1")
        minion.set_team()
        minion.move_unit()
        minion.damaged()
        if own["hp"]<=0:
            minion.die_and_gold()
