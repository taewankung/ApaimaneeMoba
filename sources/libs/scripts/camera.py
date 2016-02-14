from bge import logic
#import bpy
import bge
import Rasterizer
Rasterizer.showMouse(True)

controller = logic.getCurrentController()
scene = logic.getCurrentScene()

own = controller.owner
mouse = controller.sensors['Mouse']
key_up = controller.sensors['keybord']

#def move(position,value):
#    if position == 'x':
#        own.position.x+=value;

def move_up():
    own.position.x -=1

def move_down():
    own.position.x += 1
def move_right():
    own.position.y += 1
            
def move_left():
        own.position.y -= 1
def move_camera():
    for key,status in key_up.events:
        if key == bge.events.UPARROWKEY or key == bge.events.SKEY:
            move_up()
        if key == bge.events.DOWNARROWKEY or key == bge.events.XKEY:
            move_down()
        if key == bge.events.LEFTARROWKEY or key == bge.events.ZKEY:
            move_left() # Activate Left!
        if key == bge.events.RIGHTARROWKEY or key == bge.events.CKEY:
            move_right()  #
