from bge import logic

from libs.apaimanee.characters.minion.minion import Minion

def move():
    cont =logic.getCurrentController()
    own = cont.owner

    #checkpoint_central1 = cont.sensors["checkpoint_central1"]
    #checkpoint_central2 = cont.sensors["checkpoint_central2"]
    #checkpoint_central3 = cont.sensors["checkpoint_central3"]
    #checkpoint={"checkpoint_central1":checkpoint_central1,
    #            "checkpoint_central2":checkpoint_central2,
    #            "checkpoint_central3":checkpoint_central3}
    #move = cont.actuators["move"]
    #track = cont.actuators["track"]
    animation = cont.actuators["animation"]

#track.object=own["mempath"]
    #near = cont.sensors["near_enemy"]
    #col_enemy = cont.sensors["col_enemy"]
    #sensor_message = cont.sensors["receive_message"]
    #act_message = cont.actuators["Sender_message"]
    minion = None
    if "team2" in own:
        #print("sry")
        minion = Minion(#checkpoint,
                        cont,
                        animation,
                        own,
                        own["team2"],
                        "Armature_creep_right_team2",
                        "creep_right_action_team2"
                    #act_message,
                    #sensor_message
                        )
    else:
        minion = Minion(#checkpoint,
                        cont,
                        animation,
                        own,
                        own["team1"],
                        "Armature_creep_right_team1",
                        "creep_action_right_team1"
                    #act_message,
                    #sensor_message
                        )
    if minion != None :
        minion.set_first_path("checkpoint_right1")
        minion.set_team()
        minion.move_unit()
        minion.damaged()
        minion.die_get_gold()
       #minion.attack()
#cont.activate(command)
