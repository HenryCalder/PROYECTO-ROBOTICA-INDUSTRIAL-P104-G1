from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations
RDK = Robolink()

def TCP_On(toolitem):
    """Attaches the closest object to the toolitem Htool pose,
    It will also output appropriate function calls on the generated robot program (call to TCP_On)"""
    toolitem.AttachClosest()
    toolitem.RDK().RunMessage('Set air valve on')
    toolitem.RDK().RunProgram('TCP_On()');




PARAM_SIZE_PALLET = 'SizePallet'                    #numero de cubos

frame_conv_moving   = RDK.Item('MovingRef', ITEM_TYPE_FRAME)


#poner Ur10 A en home 
robot= RDK.Item('UR10 A',ITEM_TYPE_ROBOT)
tool=  RDK.Item('GripperA', ITEM_TYPE_TOOL)




t1= RDK.Item('CercaGet', ITEM_TYPE_TARGET) 
t2= RDK.Item('get1er', ITEM_TYPE_TARGET)                                                              #CAMBIA

t3= RDK.Item('CercaBanda', ITEM_TYPE_TARGET) 
t4= RDK.Item('En Banda', ITEM_TYPE_TARGET) 

a=RDK.getParam(PARAM_SIZE_PALLET)
a=int(a)
b=0
while (a>0):
    #MOVIMIENTOS 
    robot.MoveJ(t1)                     # se acerca a los cubos

    a2=t2.Pose()*transl(-150*b,0,0)          #posicion del cubo 

    robot.MoveJ(a2)

    TCP_On(tool)                        #recoge el cubo 
    robot.MoveJ(t1)                     # move to aproach
    robot.MoveJ(t3)                     # move approach to conveyor
    robot.MoveJ(t4)                     # put in conveyor

    tool.DetachAll(frame_conv_moving)
    robot.MoveJ(t3)                     # move to aproach table paint

              

    a-=1
    b+=1