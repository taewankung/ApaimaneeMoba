from bge import logic
controller = logic.getCurrentController()
own = controller.owner
mouse = controller.sensors["Mouse"]
#clickL = controller.sensors["clickL"]
hitPosition = mouse.hitPosition


def main(cont):
    if mouse.hitObject!=None :
        own.worldPosition.x = hitPosition.x
        own.worldPosition.y = hitPosition.y
    if str(mouse.hitObject) == "shop" and clickL.positive :
	if clickL.negative :
		print("SHOP: >Wo<!!")
    print("x= "+str(hitPosition.x))
    print("y= "+str(hitPosition.y))
    #print(mouse.hitObject)
